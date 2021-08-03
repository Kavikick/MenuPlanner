import unittest
from Singleton import Singleton

def test_getInstance():
    instance = None
    assert instance == None
    instance = Singleton.getInstance()
    assert instance
