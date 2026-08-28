"""Erkennung von Palindromen."""


def is_palindrome(text: str) -> bool:
    """Prüfe, ob ``text`` ein Palindrom ist.

    Groß-/Kleinschreibung wird ignoriert und alle Zeichen außer
    Buchstaben und Ziffern (str.isalnum) werden übersprungen.
    Ein leerer oder nur aus übersprungenen Zeichen bestehender
    String gilt als Palindrom.
    """
    letters = "".join(char for char in text if char.isalnum()).lower()
    return letters == letters[::-1]
