import pytest

from textutils.word_count import word_count


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("one two three", 3),
        ("one  two   three", 3),
        ("one\ttwo\nthree", 3),
        ("one \t two \n three", 3),
        ("", 0),
        ("   ", 0),
        ("\t\n", 0),
        ("one", 1),
    ],
)
def test_word_count(text: str, expected: int) -> None:
    assert word_count(text) == expected
