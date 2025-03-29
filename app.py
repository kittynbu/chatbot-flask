from flask import Flask, request, jsonify

app = Flask(__name__)

# 룰 베이스 응답 정의
responses = {
    "안녕": "안녕하세요! 무엇을 도와드릴까요?",
    "이름이 뭐야?": "저는 간단한 챗봇입니다.",
    "날씨 어때?": "현재 날씨 정보를 제공하지 않지만, 인터넷에서 확인해 보세요!",
}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    
    # 룰 기반 답변 찾기
    response = responses.get(user_input, "죄송해요, 이해하지 못했어요.")
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
