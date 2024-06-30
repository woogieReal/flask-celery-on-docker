# 베이스 이미지로 Python 3.9 사용
FROM python:3.9

# 작업 디렉터리 설정
WORKDIR /app

# 필요한 패키지 설치
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 앱 소스 코드를 복사
COPY . .

# Flask 서버 포트 개방
EXPOSE 5000

# 환경 변수 설정
ENV FLASK_ENV=development

# Flask 실행
# CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
CMD ["python", "app.py"]
