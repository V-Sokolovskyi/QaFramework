import pytest
from modules.api.clients.github import Github
from modules.common.database import Database
from modules.common.Alchemy_database import Database_alch


class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None
    
    def create(self):
        self.name = 'Vladyslav'
        self.second_name ='Sokolovskyi'
    
    def remove(self):
        self.name = ''
        self.second_name =''

 
        
@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = Github()
    yield api

@pytest.fixture
def database():
    db = Database()
    
    yield db

@pytest.fixture
def database_alchem():
    db = Database_alch()

    yield db

@pytest.fixture
def database_alchem_creat_delet_table():
    db = Database_alch()
    db.create_tabe(name_of_tabe="products_1")
    
    yield db

    db.delete_table(name_of_table="products_1")