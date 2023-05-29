
import requests
import allure

from utilities.logger_api import Logger

"""Список HTTP методов"""

class Http_methods:
    headers = {'Content-Type': 'application/json'} # отправка заголовков в формате json
    cookie = ""
    
    @staticmethod
    def get(url):
        with allure.step("GET"):
            Logger.add_request(url, method="GET")
            result = requests.get(url, headers= Http_methods.headers, cookies=Http_methods.cookie)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_request(url, method="POST")
            result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_request(url, method="PUT")
            result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            return result

    @staticmethod
    def delete(url):
        with allure.step("PUT"):
            Logger.add_request(url, method="DELETE")
            result = requests.delete(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
            return result

    @staticmethod
    def patch(url, body):
        with allure.step("PATCH"):
            Logger.add_request(url, method="PATH")
            result = requests.patch(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            return result
