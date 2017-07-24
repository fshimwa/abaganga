import requests
from project.exception_handling import ApiError


def make_mobile_payment(amount, phone, names):
    task = {
    "names": names,
    "phone": phone,
    "amount": amount
    }
    resp = requests.post('http://localhost:8000/mobilepayment/', json=task)
    print str(resp.status_code)+" ------------------"
    if resp.status_code != 201:
        raise ApiError('POST /tasks/ {}'.format(resp.status_code))
    print('Created task. ID: {}'.format(resp.json()["id"]))