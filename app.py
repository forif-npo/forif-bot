from flask import Flask

from routes import study_info, forif_notice

app = Flask(__name__)
app.register_blueprint(study_info.study)
app.register_blueprint(forif_notice.notice)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
