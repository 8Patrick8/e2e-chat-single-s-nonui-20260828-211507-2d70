import importlib
import inspect

import pytest

import textutils

FUNCTION_NAMES = ("slugify", "truncate", "word_count", "is_palindrome", "reverse_words")

EXPECTED_SIGNATURES = {
    "slugify": {"params": [("text", str)], "returns": str},
    "truncate": {"params": [("text", str), ("max_len", int)], "returns": str},
    "word_count": {"params": [("text", str)], "returns": int},
    "is_palindrome": {"params": [("text", str)], "returns": bool},
    "reverse_words": {"params": [("text", str)], "returns": str},
}


@pytest.mark.parametrize("name", FUNCTION_NAMES)
def test_function_importable_from_package(name: str) -> None:
    func = getattr(textutils, name)
    assert callable(func)


@pytest.mark.parametrize("name", FUNCTION_NAMES)
def test_function_lives_in_own_module(name: str) -> None:
    module = importlib.import_module(f"textutils.{name}")
    assert callable(getattr(module, name))


@pytest.mark.parametrize("name", FUNCTION_NAMES)
def test_signature_matches_contract(name: str) -> None:
    expected = EXPECTED_SIGNATURES[name]
    sig = inspect.signature(getattr(textutils, name))
    assert [(p.name, p.annotation) for p in sig.parameters.values()] == expected["params"]
    assert sig.return_annotation is expected["returns"]


def test_package_exports_every_function() -> None:
    assert set(textutils.__all__) == set(FUNCTION_NAMES)
