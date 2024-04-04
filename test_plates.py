from plates import is_valid

def main():
    value()


def test_is_valid():
    assert is_valid("AAA22A") == False
    assert is_valid("Valid") == True
    # assert is_valid("hi world") == 20
    # assert is_valid("HI WORLD") == 20
    # assert is_valid("wassup world") == 100
    # assert is_valid("WASSUP WORLD") == 100