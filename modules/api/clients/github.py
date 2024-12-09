import pytest
import requests

class Github:

    def get_user(self,username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()
        return body