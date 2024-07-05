from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import pickle

# Iris 데이터셋 로드
iris = load_iris()
X, y = iris.data, iris.target

# 클래스 분포 확인
print("Class distribution:")
for i, class_name in enumerate(iris.target_names):
    print(f"{class_name}: {np.sum(y == i)}")

# 데이터 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# stratified 샘플링을 사용한 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, stratify=y, random_state=42)

# 랜덤 포레스트 모델 생성 및 훈련
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# 모델 평가
y_pred = model.predict(X_test)
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 특성 중요도 출력
feature_importance = model.feature_importances_
for i, importance in enumerate(feature_importance):
    print(f"Feature {i+1} importance: {importance}")

# 모델 및 스케일러 저장
with open('iris_model.pkl', 'wb') as file:
    pickle.dump((model, scaler), file)

print("\nModel and scaler saved as iris_model.pkl")

# 저장된 모델 테스트
with open('iris_model.pkl', 'rb') as file:
    loaded_model, loaded_scaler = pickle.load(file)

# 각 클래스에 대한 샘플 데이터로 테스트
test_samples = np.array([
    [5.1, 3.5, 1.4, 0.2],  # 예상: setosa
    [6.7, 3.0, 5.2, 2.3],  # 예상: virginica
    [5.9, 3.0, 4.2, 1.5],  # 예상: versicolor
])

scaled_samples = loaded_scaler.transform(test_samples)
predictions = loaded_model.predict(scaled_samples)

for i, pred in enumerate(predictions):
    print(f"\nTest sample {i+1}:")
    print(f"Raw input: {test_samples[i]}")
    print(f"Scaled input: {scaled_samples[i]}")
    print(f"Prediction: {iris.target_names[pred]}")
    probabilities = loaded_model.predict_proba(scaled_samples[i].reshape(1, -1))[0]
    for j, prob in enumerate(probabilities):
        print(f"Probability of {iris.target_names[j]}: {prob:.4f}")