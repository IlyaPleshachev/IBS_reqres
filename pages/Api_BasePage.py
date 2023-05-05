from pages.BasePage import BasePage
import requests

class Api_BasePage(BasePage):
    """API functions
    - Get list users
    - Create user
    - Update user
    - Delete user"""
    def get_list_users(self):
        URL = 'https://reqres.in/api/users?page=2'
        response = requests.get(URL)
        data = {"page": 2, "per_page": 6, "total": 12, "total_pages": 2, "data": [
            {"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson",
             "avatar": "https://reqres.in/img/faces/7-image.jpg"},
            {"id": 8, "email": "lindsay.ferguson@reqres.in", "first_name": "Lindsay", "last_name": "Ferguson",
             "avatar": "https://reqres.in/img/faces/8-image.jpg"},
            {"id": 9, "email": "tobias.funke@reqres.in", "first_name": "Tobias", "last_name": "Funke",
             "avatar": "https://reqres.in/img/faces/9-image.jpg"},
            {"id": 10, "email": "byron.fields@reqres.in", "first_name": "Byron", "last_name": "Fields",
             "avatar": "https://reqres.in/img/faces/10-image.jpg"},
            {"id": 11, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards",
             "avatar": "https://reqres.in/img/faces/11-image.jpg"},
            {"id": 12, "email": "rachel.howell@reqres.in", "first_name": "Rachel", "last_name": "Howell",
             "avatar": "https://reqres.in/img/faces/12-image.jpg"}],
                "support": {"url": "https://reqres.in/#support-heading",
                            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"}}
        res_status = response.status_code
        res_json = response.json()
        return res_status, res_json


    def create_new_user(self):
        URL = "https://reqres.in/api/users"
        data = {
            "name": "morpheus",
            "job": "leader"
        }
        response = requests.post(URL, data=data)
        res_status = response.status_code
        res_json = response.json()
        assert res_status == 201, 'Status code is not 201'
        return res_status, res_json

    def update_user(self):
        URL = "https://reqres.in/api/users/2"
        data = {
            "name": "morpheus",
            "job": "zion resident"
        }
        response = requests.put(URL, data=data)
        # print(response.status_code)
        res_status = response.status_code
        res_json = response.json()
        assert res_status == 200, 'Status code is not 200'
        return res_status, res_json

    def delete_user(self):
        URL = "https://reqres.in/api/users/2"
        response = requests.delete(URL)
        res_status = response.status_code
        assert res_status == 204, 'Status code is not 204'
        return res_status
    def unhappy_register(self):
        URL = "https://reqres.in/api/register"
        data = {
            "email": "sydney@fife"
        }
        response = requests.put(URL, data=data)
        res_status = response.status_code
        assert res_status == 200, f'Status code({res_status}) is not 200'
        return res_status