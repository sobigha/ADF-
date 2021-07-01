"""Test cases"""
# from django.test import TestCase
from datetime import date
# pylint: disable=E0402
from .validateclass import ValidateClass

obj = ValidateClass()


def test_age():
    """Check the age criteria"""
    result = obj.age_criteria("male", date(1992, 6, 3))
    assert result == "Eligible"


def test_nation():
    """Check if nationality matches"""
    result = obj.nationality_criteria("indian")
    assert result == "Eligible", "nationality does not match"


def test_state():
    """Check if state matches"""
    result = obj.state_criteria("BIHAR")
    assert result == "Eligible", "State does not match"


def test_salary():
    """Check if salary matches"""
    result = obj.salary_criteria(70000)
    assert result == "Eligible", "Salary does not match"
