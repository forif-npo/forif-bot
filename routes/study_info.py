from flask import Blueprint, request

from model import database

study = Blueprint('study', __name__)


@study.route('/study', methods=['POST'])
def study_list():
    studies = database.get_study_list()

    items = list()
    for study in studies:
        item = {
            "title": study['study_name'],
            "description": study['explanation'],
            "imageUrl": study['img_url'],
            "link": {"web": study['web_url']}
        }

        items.append(item)

    output = list()
    carousel_cnt = len(items) // 5
    if len(items) % 5:
        carousel_cnt += 1

    for i in range(carousel_cnt):
        output.append(items[i*5: (i+1)*5])

    carousels = [
        {
            "type": "listCard",
            "items": carousel
        } for carousel in output
    ]

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "listCard",
                        "items": carousels
                    }
                }
            ]
        }
    }

    return response