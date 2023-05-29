
class Base():

    def __init__(self, driver): #для хранения методов(делать скрин и т.д)
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""

    def get_assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method assert url"""

    def get_assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method scroll page"""

    def get_scroll(self):
        self.driver.execute_script('window.scrollTo(0, 900)')
        print("scroll")

    """Method scroll page"""

    def get_back(self):
        self.driver.back()
        print("Возврат на главную")

    """Method refresh"""

    def get_refresh(self):
        self.driver.refresh()  # обновляем страницу
        print("Обновляем страницу")
