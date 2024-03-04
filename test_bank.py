from bank import value

def main():
    value()


def test_twttr():
    assert value("hello") == "$0"
    assert value("Hello, 20") == "$20"
    assert value("Hello, 100") == "$100"
    assert value("Cat, 100") == "$100"
