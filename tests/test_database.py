import pytest
from Database import DataBase

@pytest.fixture
def database():
    DataBase.setSourceFile('test')
    return DataBase.getInstance()

# def test_addData(database):


# def test_getData(database):

# def test_removeData(database):


# def test_saveState(database):
