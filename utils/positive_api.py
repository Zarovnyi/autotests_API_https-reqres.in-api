
from utils.http_methods import Http_methods

"""Методы для тестирования сайта Reqres"""

base_url = "https://reqres.in/api/" # Базовая URL


class Reqres_api():

    """Метод GET список пользователей"""

    @staticmethod
    def get_of_users():
        get_resource = "users?page=2"  # Ресурс метода GET список пользователей
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод GET один пользователь"""

    @staticmethod
    def get_single_user():
        get_resource = "users/2"      # Ресурс метода GET один пользователь
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод GET пользователь не найден"""

    @staticmethod
    def get_user_not_found():
        get_resource = "users/23"  # Ресурс метода GET пользователь не найден
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод GET список ресурсов"""

    @staticmethod
    def get_list_resource():
        get_resource = "unknown"  # Ресурс метода GET список ресурсов
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод GET один ресурс"""

    @staticmethod
    def get_single_resource():
        get_resource = "unknown/2"  # Ресурс метода GET один ресурс
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод GET ресурс не найден"""

    @staticmethod
    def get_resource_not_found():
        get_resource = "unknown/23"  # Ресурс метода GET ресурс не найден
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод POST для создания пользователя"""

    @staticmethod
    def create_new_place():
        json_create_user = {
            "name": "morpheus",
            "job": "leader"
        }

        post_resource = "user"  # Ресурс метода Post
        post_url = base_url + post_resource
        print(post_url)
        result_post = Http_methods.post(post_url, json_create_user)
        print(result_post.text)
        return result_post

    """Метод PUT для обновления"""

    @staticmethod
    def put_update():
        json_update_user = {
            "name": "morpheus",
            "job": "leader"
        }
        put_resource = "users/2"  # Ресурс метода PUT обновить
        put_url = base_url + put_resource
        print(put_url)
        result_put = Http_methods.put(put_url, json_update_user)
        print(result_put.text)
        return result_put

    """Метод PATCH для обновления"""

    @staticmethod
    def patch_update():
        json_patch_update_user = {
            "name": "morpheus",
            "job": "zion resident"
        }
        patch_resource = "users/1"         # Ресурс метода PATCH обновить
        patch_url = base_url + patch_resource
        print(patch_url)
        result_patch = Http_methods.patch(patch_url, json_patch_update_user)
        print(result_patch.text)
        return result_patch

    """Метод DELETE"""

    @staticmethod
    def delete():
        delete_resource = "users/10"  # Ресурс метода DELETE
        delete_url = base_url + delete_resource
        print(delete_url)
        result_delete = Http_methods.delete(delete_url)
        print(result_delete.text)
        return result_delete

    """Метод POST успешная регистрация"""

    @staticmethod
    def register_successful():
        json_register_successful = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }

        post_resource = "register"  # Ресурс метода Post  успешная регистрация
        post_url = base_url + post_resource
        print(post_url)
        result_post = Http_methods.post(post_url, json_register_successful)
        print(result_post.text)
        return result_post

    """Метод POST неудачная регистрация"""

    @staticmethod
    def register_unsuccessful():
        json_register_unsuccessful = {
            "email": "sydney@fife"
        }

        post_resource = "register"  # Ресурс метода Post  неудачная регистрация
        post_url = base_url + post_resource
        print(post_url)
        result_post = Http_methods.post(post_url, json_register_unsuccessful)
        print(result_post.text)
        return result_post

    """Метод POST успешный вход в систему"""

    @staticmethod
    def login_successful():
        json_login_successful = {
             "email": "eve.holt@reqres.in",
             "password": "cityslicka"
        }

        post_resource = "login"  # Ресурс метода Post успешный вход в систему
        post_url = base_url + post_resource
        print(post_url)
        result_post = Http_methods.post(post_url, json_login_successful )
        print(result_post.text)
        return result_post

    """Метод POST неудачный вход в систему"""

    @staticmethod
    def login_unsuccessful():
        json_login_unsuccessful = {
            "email": "peter@klaven"
        }

        post_resource = "login"  # Ресурс метода Post неудачный вход в систему
        post_url = base_url + post_resource
        print(post_url)
        result_post = Http_methods.post(post_url, json_login_unsuccessful)
        print(result_post.text)
        return result_post

    """Метод GET запоздалый ответ"""

    @staticmethod
    def get_delayed_response():
        get_resource = "users?delay=3"  # Ресурс метода GET запоздалый ответ
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get
