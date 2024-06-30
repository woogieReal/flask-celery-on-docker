from database import db_session, init_db
from flask import Flask, request, jsonify
from celery import Celery
from sqlalchemy import desc
from flask_cors import CORS
from models import APILog
import os

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config['CELERY_BROKER_URL'] = os.environ['CELERY_BROKER_URL']
app.config['CELERY_RESULT_BACKEND'] = os.environ['CELERY_RESULT_BACKEND']

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def process_data(data):
    print("process_data", flush=True)
    new_entry = APILog(
        api_request=data.get("api_request"),
        api_response=data.get("api_response"),
    )
    print(new_entry, flush=True)
    db_session.add(new_entry)
    db_session.commit()
    return 'Data processed and saved to MySQL'

@app.route('/add_to_queue', methods=['POST'])
def add_to_queue():
    print("add_to_queue", flush=True)
    print(request.json, flush=True)
    api_info = {
        "api_request": request.json['apiRequest'],
        "api_response": request.json['apiResponse'],
    }
    print(api_info, flush=True)
    process_data.delay(api_info)
    return jsonify({'message': 'Data added to queue'}), 202

@app.route('/api_logs', methods=['GET'])
def get_api_logs():
   # 세션을 통해 데이터베이스에서 모든 로그 조회
    logs = db_session.query(APILog).order_by(desc(APILog.creation_date)).all()
    # 조회된 로그를 리스트로 변환
    logs_list = [
        {
            'logId': log.log_id,
            'apiRequest': log.api_request,
            'apiResponse': log.api_response,
            'creationDate': log.creation_date
        } for log in logs
    ]
    return jsonify(logs_list)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0')
