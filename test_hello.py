from hello import more_hello, more_goodbye


def test_more_hello():
    assert "hi" == more_hello()


# def test_more_hello_failure():
#     assert "hola" == more_hello()


def test_more_goodbye():
    assert "bye" == more_goodbye()


# def test_more_goodbye_failure():
#     assert "goodby" == more_goodbye()