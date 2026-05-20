import requests


class APIHelper:

    @staticmethod
    def get(url, headers=None):
        return requests.get(url, headers=headers)

    @staticmethod
    def post(url, payload=None, headers=None):
        return requests.post(url, json=payload, headers=headers)

    @staticmethod
    def put(url, payload=None, headers=None):
        return requests.put(url, json=payload, headers=headers)

    @staticmethod
    def delete(url, headers=None):
        return requests.delete(url, headers=headers)