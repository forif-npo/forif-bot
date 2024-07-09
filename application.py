from flask import Flask, request, jsonify

from routes import study_info, forif_notice

app = Flask(__name__)
app.register_blueprint(study_info.study)
app.register_blueprint(forif_notice.notice)

@app.errorhandler(500)
def server_error(error):
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "textCard": {
                        "title": "🦊 챗봇 서버에 오류가 발생했습니다.",
                        "buttons": [
                            {
                                "action": "webLink",
                                "label": "웹사이트에서 보기",
                                "webLinkUrl": "https://www.forif.org/"
                            }
                        ]
                    }
                }
            ]
        }
    }

    return response



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
