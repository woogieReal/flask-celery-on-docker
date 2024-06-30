# 베이스 이미지로 Node.js 22 사용
FROM node:22

# 애플리케이션 디렉터리 생성
WORKDIR /usr/src/app

# 패키지 설치를 위해 package.json과 package-lock.json 복사
COPY package*.json ./

# 의존성 설치
RUN npm install

# 앱 소스 코드를 복사
COPY . .

# 개발 서버 포트 개방
EXPOSE 3000

# 개발 모드에서 앱 실행
CMD ["npm", "start"]
