from plates import is_valid

def main():
    value()


def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("50") == False