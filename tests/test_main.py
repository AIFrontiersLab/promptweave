"""Tests for Intent Classifier."""
import pytest
from main import classify_intent, demo

def test_classify_refactor():
    assert classify_intent("refactor this code")['intent'] == 'code_refactor'

def test_classify_test():
    assert classify_intent("write tests")['intent'] == 'test_generation'

def test_classify_docs():
    assert classify_intent("add docs")['intent'] == 'documentation'

def test_classify_unknown():
    assert classify_intent("hello")['intent'] == 'unknown'

def test_demo_function():
    result = demo()
    assert result == "code_refactor"