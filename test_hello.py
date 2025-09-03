from hello import say_hello, add


def test_say_hello():
    assert (
        say_hello("Annie")
        == "Hello, Annie, welcome to Duke and hope you have a great day!"
    )


def test_add():
    assert add(5, 6) == 11
