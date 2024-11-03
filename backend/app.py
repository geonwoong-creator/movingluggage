# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Vue와 통신하기 위해 CORS 설정

@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/reserve', methods=['POST'])
def reserve():
    data = request.get_json()  # Vue에서 전송된 JSON 데이터를 받음
    # 예시로 데이터를 출력해봅니다.
    print("Received reservation data:", data)
    
    # 여기서 데이터베이스에 저장하거나 다른 처리를 할 수 있습니다.
    # 지금은 간단히 확인 메시지를 반환합니다.
    return jsonify({"message": "Reservation received", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True)