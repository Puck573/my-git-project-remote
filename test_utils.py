import pytest
import utils

def test_is_even():
    assert utils.is_even(2) == True
    assert utils.is_even(3) == False
    assert utils.is_even(0) == True

def test_generate_password():
    password = utils.generate_password(10)
    assert len(password) == 10
    
    password2 = utils.generate_password(10)
    assert password != password2  # С большой вероятностью пароли разные
