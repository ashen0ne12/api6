import requests

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_users(self):
        response = requests.get(f"{self.BASE_URL}/users")
        return response
