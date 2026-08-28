from textutils.slugify import slugify


def test_slugify_core_case() -> None:
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_multiple_spaces_and_punctuation() -> None:
    assert slugify("  Foo--Bar!  ") == "foo-bar"


def test_slugify_collapses_consecutive_separators() -> None:
    assert slugify("a   b...c__d") == "a-b-c-d"


def test_slugify_empty_string() -> None:
    assert slugify("") == ""


def test_slugify_only_separators() -> None:
    assert slugify(" !!!  --- ") == ""
