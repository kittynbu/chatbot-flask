from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS 활성화 (프론트엔드에서 API 호출 가능)

# 🔹 챗봇의 룰 기반 응답 설정
rule_based_responses = {
    "안녕": "안녕하세요! 무엇을 도와드릴까요?",
    "이름이 뭐야?": "저는 룰 기반 챗봇입니다.",
    "날씨 어때?": "날씨 정보는 제공하지 않지만, 오늘 하루 즐겁게 보내세요!",
    "몇 살이야?": "저는 나이가 없지만 언제나 배울 준비가 되어 있어요.",
    "잘 가": "좋은 하루 되세요! 다음에 또 만나요."
}

# 🔹 기본 응답 (룰에 없는 입력 처리)
default_response = "죄송해요, 이해하지 못했어요. 다른 질문을 해주세요."

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # 요청에서 JSON 데이터 가져오기
        data = request.json
        if not data or "message" not in data:
            return jsonify({"error": "올바른 입력이 아닙니다."}), 400

        user_message = data["message"].strip()  # 앞뒤 공백 제거

        # 룰 기반 응답 찾기
        response_text = rule_based_responses.get(user_message, default_response)

        return jsonify({"response": response_text})  # JSON 응답 반환

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # 서버 오류 발생 시 처리

if __name__ == "__main__":
    app.run(debug=True)
