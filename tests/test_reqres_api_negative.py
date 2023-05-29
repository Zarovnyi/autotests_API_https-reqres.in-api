
from utils.cheking import Сhecking
from utils.negative_api import Reqres_api
import allure

"""Негативная проверка"""

@allure.epic("Негативная проверка ")
class Test_negative_verification():

    @allure.description("Негативная проверка GET список пользователей")
    def test_of_userse(self):
        print("Метод GET список пользователей")
        result_get = Reqres_api.get_of_users()
        Сhecking.check_status_code(result_get, 200) # для проверки статус кода

    @allure.description("Негативная проверка GET один пользователь")
    def test_single_user(self):
        print("Метод GET один пользователь")
        result_get = Reqres_api.get_single_user()
        Сhecking.check_status_code(result_get, 200)

    @allure.description("Негативная проверка GET пользователь не найден")
    def test_user_not_found(self):
        print("Метод GET пользователь не найден")
        result_get = Reqres_api.get_user_not_found()
        Сhecking.check_status_code(result_get, 404)

    @allure.description("Негативная проверка GET список ресурсов")
    def test_list_resource(self):
        print("Метод GET список ресурсов")
        result_get = Reqres_api.get_list_resource()
        Сhecking.check_status_code(result_get, 200)

    @allure.description("Негативная проверка GET один ресурс")
    def test_single_resource(self):
        print("Метод GET один ресурс")
        result_get = Reqres_api.get_single_resource()
        Сhecking.check_status_code(result_get, 200)

    @allure.description("Негативная проверка GET ресурс не найден")
    def test_resource_not_found(self):
        print("Метод GET  ресурс не найден")
        result_get = Reqres_api.get_resource_not_found()

    @allure.description("Негативная проверка POST для создания пользователя")
    def test_creat_new_place(self):
        print("Метод POST для создания пользователя")
        result_post = Reqres_api.create_new_place()
        Сhecking.check_status_code(result_post, 201)

    @allure.description("Негативная проверка PUT для обновления")
    def test_put_update(self):
        print("Метод PUT для обновления")
        result_put = Reqres_api.put_update()
        Сhecking.check_status_code(result_put, 200)

    @allure.description("Негативная проверка PATCH для обновления")
    def test_patch_update(self):
        print("Метод PATCH для обновления")
        result_patch = Reqres_api.patch_update()
        Сhecking.check_status_code(result_patch, 404)

    @allure.description("Негативная проверка DELETE")
    def test_delete(self):
        print("Метод DELETE")
        result_delete = Reqres_api.delete()
        Сhecking.check_status_code(result_delete, 404)

    @allure.description("Негативная проверка POST успешная регистрация")
    def test_register_successful(self):
        print("Метод POST успешная регистрация")
        result_post = Reqres_api.register_successful()
        Сhecking.check_status_code(result_post, 404)

    @allure.description("Негативная проверка POST неудачная регистрация")
    def test_register_unsuccessful(self):
        print("Метод POST неудачная регистрация")
        result_post = Reqres_api.register_unsuccessful()
        Сhecking.check_status_code(result_post, 400)

    @allure.description("Негативная проверка POST успешный вход в систему")
    def test_login_successful(self):
        print("Метод POST успешный вход в систему")
        result_post = Reqres_api.login_successful()
        Сhecking.check_status_code(result_post, 404)

    @allure.description("Негативная проверка POST неудачный вход в систему")
    def test_login_unsuccessful(self):
        print("Метод POST  неудачный вход в систему")
        result_post = Reqres_api.login_unsuccessful()
        Сhecking.check_status_code(result_post, 400)\

    @allure.description("Негативная проверка GET запоздалый ответ")
    def test_get_delayed_response(self):
        print("Метод GET запоздалый ответ")
        result_get = Reqres_api.get_delayed_response()
        Сhecking.check_status_code(result_get, 404)

        print("Тестирование негативная проверка API прошло успешно")
