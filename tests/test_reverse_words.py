import pytest

from textutils.reverse_words import reverse_words


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("one two three", "three two one"),
        ("one", "one"),
        ("", ""),
    ],
)
def test_reverse_words_kehrt_wortreihenfolge_um(text: str, expected: str) -> None:
    assert reverse_words(text) == expected


def test_reverse_words_reduziert_mehrfach_leerzeichen_zu_einfachen() -> None:
    assert reverse_words("one   two \t three") == "three two one"


def test_reverse_words_laesst_buchstaben_unveraendert() -> None:
    assert reverse_words("abc def") == "def abc"
