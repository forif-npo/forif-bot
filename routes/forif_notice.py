from flask import Blueprint, request, jsonify

from model import database

notice = Blueprint('notice', __name__)


@notice.route('/notice', methods=['POST'])
def study_list():
    notices = database.get_recent_notice()

    items = list()
    for notice in notices:
        item = {
            "title": notice['notice_title'],
            "description": "게시 날짜 : " + notice['notice_date'],
            "link": {"web": "https://www.forif.org/"}
        }
        items.append(item)

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "🦊 최근 올라온 공지사항들"
                        },
                        "items": items
                    }
                }
            ]
        }
    }

    return response