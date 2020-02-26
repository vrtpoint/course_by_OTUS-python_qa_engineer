"""Тесты методов api сайта https://api.openbrewerydb.org/"""

class TestBreweryDb:
    """Класс для тестирования методов api сайта https://api.openbrewerydb.org/"""

    def test_check_brewery_list(self, response_brewery_list):
        """Тест проверяет налачие списка пивоварен"""
        assert response_brewery_list != []
        print(response_brewery_list)

    def test_check_brewery_response_status(self, response_brewery_status):
        """Тест проверяет код успешности ответа от полуения списка пиоварен """
        assert response_brewery_status == 200
        print(response_brewery_status)

    def test_check_brewery_by_state(self, response_brewery_by_state):
        """Тест проверяет наличие пивоварен по выбранному штату"""
        assert response_brewery_by_state != []
        assert response_brewery_by_state[0]['state'] == "New York"
        print(response_brewery_by_state)

    def test_check_brewery_by_name(self, response_brewery_by_name):
        """Тест проверяет по выбранному имени"""
        assert response_brewery_by_name != []
        assert response_brewery_by_name[0]['name'] == "Yellowhammer Brewery"
        print(response_brewery_by_name)

    def test_check_brewery_by_tag(self, response_brewery_by_tag):
        """Тест проверяет по выбранному тегу"""
        assert response_brewery_by_tag != []
        assert response_brewery_by_tag[0]['tag_list'][0] == "patio"
        print(type(response_brewery_by_tag[0]))