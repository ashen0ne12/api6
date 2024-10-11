import pytest
from client import APIClient


class TestAPIClient:
    client = APIClient()

    def test_get_users_status_code(self):
        response = self.client.get_users()
        assert response.status_code == 200

    def test_get_users_success(self):
        response = self.client.get_users()
        users = response.json()
        assert len(users) > 0

    def test_users_fields(self):
        response = self.client.get_users()
        users = response.json()

        for user in users:
            assert 'id' in user
            assert 'name' in user
            assert 'username' in user
            assert 'email' in user

    def test_users_email_format(self):
        response = self.client.get_users()
        users = response.json()

        for user in users:
            email = user['email']
            assert '@' in email
