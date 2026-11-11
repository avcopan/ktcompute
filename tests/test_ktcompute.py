"""ktcompute tests."""

import ktcompute


def test_stub() -> None:
    """Stub test to ensure the test suite runs."""
    print(ktcompute.__version__)  # noqa: T201


def test__greet() -> None:
    """Test the greet function."""
    assert ktcompute.greet("World") == "Hello, World!"


def test__greet_jim() -> None:
    """Test the greet_jim function."""
    assert ktcompute.greet_jim() == "Hello, Jim!"
