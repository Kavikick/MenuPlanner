import unittest
from Singleton import Singleton

def test_getInstance():
    instance = None
    assert instance == None
    instance = Singleton.getInstance()
    assert instance

def test_getSameInstance():
    instance1 = Singleton.getInstance()
    instance2 = Singleton.getInstance()
    assert instance1 is instance2
