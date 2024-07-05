import requests
import json

# API 엔드포인트 URL
url = "http://localhost:5001/predict"

# 예측하고자 하는 샘플 데이터
sample_data = [
    [5.1, 3.5, 1.4, 0.2],  # 예상: setosa
    [6.7, 3.0, 5.2, 2.3],  # 예상: virginica
    [5.9, 3.0, 4.2, 1.5],  # 예상: versicolor
]

# Iris 클래스 이름 (참조용)
iris_classes = ['setosa', 'versicolor', 'virginica']

# 각 샘플에 대해 예측 수행
for i, features in enumerate(sample_data):
    # API 요청 데이터 준비
    data = {
        "features": features
    }

    try:
        # POST 요청 보내기
        response = requests.post(url, json=data)
        
        # 응답 상태 코드 확인
        response.raise_for_status()

        # JSON 응답 파싱
        result = response.json()

        # 결과 출력
        print(f"\nSample {i+1}:")
        print(f"Input features: {features}")
        print(f"Predicted class: {iris_classes[result['prediction']]}")
        print("Class probabilities:")
        for j, prob in enumerate(result['probabilities']):
            print(f"  {iris_classes[j]}: {prob:.4f}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
    except json.JSONDecodeError:
        print("Failed to decode the JSON response from the server.")
    except KeyError:
        print("The server response doesn't contain the expected keys.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")