
from utils.cheking import Сhecking
from utils.positive_api import Reqres_api
import allure

"""Позитивная проверка  API"""

@allure.epic("Позитивная проверка  API")
class Test_positive_verification():

    @allure.description("GET список пользователей")
    def test_of_userse(self):
        print("Метод GET список пользователей")
        result_get = Reqres_api.get_of_users()
        Сhecking.check_status_code(result_get, 200) # для проверки статус кода
        Сhecking.check_json_token(result_get, ['page', 'per_page', 'total', 'total_pages', 'data', 'support']) # для проверки наличия обязательных полей в ответе запроса
        Сhecking.check_json_value(result_get, 'page', 2)  # для проверки значения обязательных полей в ответе запроса

    @allure.description("GET один пользователь")
    def test_single_user(self):
        print("Метод GET один пользователь")
        result_get = Reqres_api.get_single_user()
        Сhecking.check_status_code(result_get, 200)
        Сhecking.check_json_token(result_get, ['data','support'])

    @allure.description(" GET пользователь не найден")
    def test_user_not_found(self):
        print("Метод GET пользователь не найден")
        result_get = Reqres_api.get_user_not_found()
        Сhecking.check_status_code(result_get, 404)

    @allure.description(" GET список ресурсов")
    def test_list_resource(self):
        print("Метод GET список ресурсов")
        result_get = Reqres_api.get_list_resource()
        Сhecking.check_status_code(result_get, 200)
        Сhecking.check_json_token(result_get, ['page', 'per_page', 'total', 'total_pages', 'data', 'support'])
        Сhecking.check_json_value(result_get, 'page', 1)

    @allure.description(" GET  один ресурс")
    def test_single_resource(self):
        print("Метод GET  один ресурс")
        result_get = Reqres_api.get_single_resource()
        Сhecking.check_status_code(result_get, 200)
        Сhecking.check_json_token(result_get, ['data', 'support'])

    @allure.description(" GET  ресурс не найден")
    def test_resource_not_found(self):
        print("Метод GET  ресурс не найден")
        result_get = Reqres_api.get_resource_not_found()
        Сhecking.check_status_code(result_get, 404)
        Сhecking.check_json_token(result_get, [])

    @allure.description(" POST для создания пользователя")
    def test_creat_new_place(self):
        print("Метод POST для создания пользователя")
        result_post = Reqres_api.create_new_place()
        Сhecking.check_status_code(result_post, 201)
        Сhecking.check_json_token(result_post, ['name', 'job', 'id', 'createdAt'])
        Сhecking.check_json_value(result_post, 'name', 'morpheus')

    @allure.description(" PUT для обновления")
    def test_put_update(self):
        print("Метод PUT для обновления")
        result_put = Reqres_api.put_update()
        Сhecking.check_status_code(result_put, 200)
        Сhecking.check_json_token(result_put, ['name', 'job', 'updatedAt'])
        Сhecking.check_json_value(result_put, 'name', 'morpheus')

    @allure.description(" PATCH для обновления")
    def test_patch_update(self):
        print("Метод PATCH для обновления")
        result_patch = Reqres_api.patch_update()
        Сhecking.check_status_code(result_patch, 200)
        Сhecking.check_json_token(result_patch, ['name', 'job', 'updatedAt'])
        Сhecking.check_json_value(result_patch, 'name', 'morpheus')

    @allure.description(" етод DELETE")
    def test_delete(self):
        print("Метод DELETE")
        result_delete = Reqres_api.delete()
        Сhecking.check_status_code(result_delete, 204)

    @allure.description(" POST успешная регистрация")
    def test_register_successful(self):
        print("Метод POST успешная регистрация")
        result_post = Reqres_api.register_successful()
        Сhecking.check_status_code(result_post, 200)
        Сhecking.check_json_token(result_post, ['id', 'token'])
        Сhecking.check_json_value(result_post, 'id', 4)

    @allure.description(" POST неудачная регистрация")
    def test_register_unsuccessful(self):
        print("Метод POST неудачная регистрация")
        result_post = Reqres_api.register_unsuccessful()
        Сhecking.check_status_code(result_post, 400)
        Сhecking.check_json_token(result_post, ['error'])
        Сhecking.check_json_value(result_post, 'error', 'Missing password')

    @allure.description(" POST успешный вход в систему")
    def test_login_successful(self):
        print("Метод POST успешный вход в систему")
        result_post = Reqres_api.login_successful()
        Сhecking.check_status_code(result_post, 200)
        Сhecking.check_json_token(result_post, ['token'])
        Сhecking.check_json_value(result_post, 'token', 'QpwL5tke4Pnpja7X4')

    @allure.description(" POST  неудачный вход в систему")
    def test_login_unsuccessful(self):
        print("Метод POST  неудачный вход в систему")
        result_post = Reqres_api.login_unsuccessful()
        Сhecking.check_status_code(result_post, 400)
        Сhecking.check_json_token(result_post, ['error'])
        Сhecking.check_json_value(result_post, 'error', 'Missing password') # для проверки значения обязательных полей в ответе запроса

    @allure.description(" GET GET запоздалый ответ")
    def test_get_delayed_response(self):
        print("Метод GET запоздалый ответ")
        result_get = Reqres_api.get_delayed_response()
        Сhecking.check_status_code(result_get, 200)

        print("Тестирование позитивной проверки API прошли успешно")
