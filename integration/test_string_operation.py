import string_operation


def test_capitalize_string():
    assert string_operation.capitalize_string("hello") == "Hello"
def test_capitalize_string():
    assert string_operation.capitalize_string("python") == "Python"
def test_capitalize_string():
    assert string_operation.capitalize_string("hello world") == "Hello world"


def test_reverse_string():

    assert string_operation.revers_string("hello") == "o1lleh"
    assert string_operation.revers_string("python") == "nohtyp"
    assert string_operation.revers_string("hello world") == "dlrow olleh"
