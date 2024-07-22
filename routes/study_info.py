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

    carousel_count = len(items) // 5
    if len(items) % 5:
        carousel_count += 1

    result = list()
    for i in range(carousel_count):
        temp = {
            "items": items[i*5 : (i+1) * 5]
        }

        result.append(temp)

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "listCard",
                        "items": [
                            {
                                "items": items[0:5]
                            },
                            {
                                "items": items[5:10]
                            },
                            {
                                "items": items[10:15]
                            }
                        ]
                    }
                }
            ]
        }
    }

    return response