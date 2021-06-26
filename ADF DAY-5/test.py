from datetime import date
import pytest
from main import Details

obj = Details()
def test_age():
    result = obj.age_criteria("male",date(1992,6,3))
    assert result == "Eligible"

def test_nation():
    result = obj.nationality_criteria("indian")
    assert result == "Eligible"

def test_state():
    result = obj.state_criteria("BIHAR")
    assert  result == "Eligible"

def test_salary():
    result = obj.salary_criteria(20000)
    assert result == "Eligible"

def test_pan():
    result = obj.check_date("2021-5-17","tvxp89i")
    assert result == "Eligible"











