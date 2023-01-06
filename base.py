from requests import get, post
from secrets import HACK_ATTIC_TOKEN
import json


class Problem:
    BASE_URL = 'https://hackattic.com'
    ACCESS_TOKEN = HACK_ATTIC_TOKEN

    def __init__(self, name, playground=False):
        self.question_endpoint = self.BASE_URL + '/challenges/' + name + '/problem' + f"?access_token={self.ACCESS_TOKEN}"
        self.answer_endpoint = self.BASE_URL + '/challenges/' + name + '/solve'  f"?access_token={self.ACCESS_TOKEN}"
        if playground:
            self.question_endpoint += '&playground=1'
            self.answer_endpoint += '&playground=1'

    def get_question(self):
        response = get(self.question_endpoint)
        return json.loads(response.content)

    def send_answer(self, body):
        response = post(self.answer_endpoint, json=body)
        print(response.content)
        return response
