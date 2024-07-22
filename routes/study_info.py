from flask import Blueprint, request, jsonify

from model import database

study = Blueprint('study', __name__)


@study.route('/study', methods=['POST'])
def study_list():
    studies = database.get_study_list()

    for study in studies:
        item = {
            "title": study['study_name'],
            "description": study['explanation'],
            "imageUrl": study['img_url'],
            "link": {"web": study['web_url']}
        }

        items.append(item)

    output = list()
    carosel = len(items) // 5
    if len(items) % 5:
        carosel += 1

    for i in range(carosel):
        output.append(items[i*5 : (i+1)]*5)

    response = {
        "version": "2.0",
        "template": {
            "outputs": output
        }
    }

    return response