def say_hello(name: str) -> str:
    """Return a greeting message to Annie."""
    return f"Hello, {name}, welcome to Duke and hope you have a great day!"


def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    print(say_hello("Annie"))
    print(f"5 + 6 = {add(5, 6)}")
