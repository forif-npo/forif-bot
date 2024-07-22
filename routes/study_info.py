from flask import Blueprint, request, jsonify

from model import database

study = Blueprint('study', __name__)


@study.route('/study', methods=['POST'])
def study_list():
    studies = database.get_study_list()

    items_1 = list()

    for study in studies:
        item = {
            "title": study['study_name'],
            "description": study['explanation'],
            "imageUrl": study['img_url'],
            "link": {"web": study['web_url']}
        }

        items.append(item)

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "🦊 현재 운영 중인 정규 스터디"
                        },
                        "items": items[0:5]
                    }
                },
                {
                    "listCard": {
                        "header": {
                            "title": "🦊 현재 운영 중인 정규 스터디"
                        },
                        "items": items[5:10]
                    }
                }
            ]
        }
    }

    return response