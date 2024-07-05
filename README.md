# devmlops-msa 프로젝트

이 프로젝트는 7/9(화) 진행될 DevOps, MLOps 실습 예제코드와 7/16(화) 진행될 Microservice, MSA 실습 예제코드가 포함되어 있습니다.

## 1. DevOps, MLOps 실습 (7/9 화)

### MLOps

#### inference-test
- `app.py`: 추론 API 애플리케이션
- `model.pkl`: 저장된 머신러닝 모델
- `test_api.py`: API 테스트 스크립트
- `train_model.py`: 모델 학습 스크립트

#### jupyter-notebook-test
- `jupyter-ml-test.ipynb`: Jupyter 노트북을 사용한 머신러닝 테스트
- `model-train-deploy.ipynb`: 모델 학습 및 배포 과정을 보여주는 주피터 노트북 코드

## 2. Microservice, MSA 실습 (7/16 화)

### microservice-container
Spring Boot 기반의 마이크로서비스 예제입니다.

- `Dockerfile`: 컨테이너 이미지 빌드 설정
- `build.gradle`, `settings.gradle`: Gradle 빌드 설정
- `src/main/java`: Java 소스 코드
- `src/main/resources`: 정적 리소스 및 설정 파일

### msa-cicd
마이크로서비스 아키텍처의 CI/CD 예제입니다.

- `db`: 데이터베이스 설정
  - `Dockerfile`: DB 컨테이너 이미지 설정
  - `init.sql`: 초기 DB 스크립트
- `was`: 애플리케이션 서버
  - `Dockerfile`: WAS 컨테이너 이미지 설정
  - `app.py`: Python 기반 애플리케이션
  - `requirements.txt`: Python 의존성 목록
- `web`: 웹 서버
  - `Dockerfile`: 웹 서버 컨테이너 이미지 설정
  - `index.html`: 메인 페이지
  - `nginx.conf`: Nginx 설정 파일