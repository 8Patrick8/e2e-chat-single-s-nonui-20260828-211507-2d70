import pytest

from textutils.is_palindrome import is_palindrome


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("A man, a plan, a canal: Panama", True),
        ("abcba", True),
        ("AbBa", True),
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon", True),
        ("12321", True),
        ("", True),
        ("   ", True),
        (",.:;!?", True),
        ("hello", False),
        ("palindrome", False),
        ("aabb", False),
    ],
)
def test_is_palindrome(text: str, expected: bool) -> None:
    assert is_palindrome(text) is expected
