import pytest

from textutils.truncate import truncate


@pytest.mark.parametrize(
    ("text", "max_len", "expected"),
    [
        ("Hallo Welt", 7, "Hallo …"),
        ("Hallo Welt", 5, "Hall…"),
        ("Hallo", 4, "Hal…"),
        ("abc", 3, "abc"),
        ("H", 1, "H"),
        ("ab", 1, "…"),
    ],
)
def test_truncate_kernel_and_edge_cases(text: str, max_len: int, expected: str) -> None:
    assert truncate(text, max_len) == expected


@pytest.mark.parametrize(
    ("text", "max_len"),
    [
        ("", 1),
        ("Hallo Welt", 10),
        ("Hallo", 6),
    ],
)
def test_truncate_short_text_unchanged(text: str, max_len: int) -> None:
    assert truncate(text, max_len) == text


def test_truncate_never_exceeds_max_len() -> None:
    result = truncate("Ein sehr langer Text", 9)
    assert len(result) <= 9
    assert result.endswith("\u2026")


@pytest.mark.parametrize("max_len", [0, -1, -100])
def test_truncate_invalid_max_len_raises_value_error(max_len: int) -> None:
    with pytest.raises(ValueError):
        truncate("Hallo Welt", max_len)
