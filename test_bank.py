from bank import value

def main():
    value()


def test_twttr():
    assert value("Hello, 20") == "$20"
    assert value("Hello, 100") == "$100"
    assert value("WorD") == "WrD"
    assert value("1234") == "1234"
    assert value(".!?,") == ".!?,"