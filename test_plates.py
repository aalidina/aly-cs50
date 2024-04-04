from plates import is_valid

def main():
    value()


def test_is_valid():
    # “All vanity plates must start with at least two letters.”

    assert is_valid("50") == False
    assert is_valid("H") == False

    # “Numbers cannot be used in the middle of a plate; they must come at the end.
    #  For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    # The first number used cannot be a ‘0’.”
    assert is_valid("CS50") == True
    
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
     assert is_valid("OUTATIME") == False

    # “No periods, spaces, or punctuation marks are allowed.”
    assert is_valid("PI3.14") == False


