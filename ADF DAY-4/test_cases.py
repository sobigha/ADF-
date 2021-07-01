import pytest
from test_file import *

obj = TestChild()


def test_toprefix():
    """Check if both results are true"""
    res1 = obj.prefix_word()
    res2 = ['to', 'together']
    assert res1 == res2


def test_suffix():
    """Check if both results are true"""
    result_first = obj.suffix_word()
    result_check = ['coming', 'going']
    assert result_first == result_check


def test_maximum():
    """Check if both results are true"""
    result_first = obj.maximum_words()
    result_check = 'cab'
    assert result_first == result_check


def test_palindrome():
    """Check if both results are true"""
    result_first = obj.palindrome_words()
    result_check = ['madam']
    assert result_first == result_check


def test_unique():
    """Check if both results are true"""
    result_first = obj.unique_list()
    result_check = ['to', 'together', 'coming', 'going', 'cab', 'madam']
    assert result_first == result_check


def test_dictword():
    """Check if both results are true"""
    result_first = obj.dict_word()
    result_check = [(0, 'to'), (1, 'together'), (2, 'coming'), (3, 'going'), \
                    (4, 'cab'), (5, 'cab'), (6, 'madam')]
    assert result_first == result_check


def test_vowels():
    """Check if both results are true"""
    result_first = obj.vowels()
    result_check = 7
    assert result_first == result_check


def test_capitalthird():
    """Check if both results are true"""
    result_first = obj.capitalize_thirdletter()
    result_check = 'to toGether coMing goIng caB caB maDam '
    assert result_first == result_check


def test_capitalfifth():
    """Check if both results are true"""
    result_first = obj.capitalize_5thword()
    result_check = 'together coming going cab CAB madam '
    assert result_first == result_check


def test_hyphen():
    """Check if both results are true"""
    result_first = obj.hyphen()
    result_check = 'to-together-coming-going-cab-cab-madam'
    assert result_first == result_check


def test_semicolon():
    """Check if both results are correct"""
    result_first = obj.semicolon()
    result_check = 'to together coming going cab cab madam'
    assert result_first == result_check
