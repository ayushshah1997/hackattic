import math
import json
from hashlib import sha256
from base import Problem

question_endpoint = '/challenges/mini_miner/problem'
answer_endpoint = '/challenges/mini_miner/solve'
p = Problem(question_endpoint=question_endpoint, answer_endpoint=answer_endpoint)

body = p.get_question()
difficulty = body['difficulty']
block = body['block']
nonce = 0


def check_first_n_bits(string, n):
    # Convert the string to a binary string
    return string.startswith('0' * math.ceil(n / 4))


while True:
    block['nonce'] = nonce
    sha = sha256(
        json.dumps({"data": block['data'], "nonce": nonce}, separators=(',', ':')).strip().encode()).hexdigest()
    if check_first_n_bits(sha, difficulty):
        data = {'nonce': nonce}
        p.send_answer(data)
        exit(0)
    else:
        nonce += 1
