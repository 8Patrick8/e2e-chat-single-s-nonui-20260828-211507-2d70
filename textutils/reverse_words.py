"""Umkehrung der Wortreihenfolge in einem String."""


def reverse_words(text: str) -> str:
    """Drehe die Wortreihenfolge in ``text`` um.

    Die Buchstaben bleiben unverändert; nur die Reihenfolge der Wörter wird
    umgekehrt. Mehrfach-Leerzeichen werden auf einfache Leerzeichen reduziert;
    ein leerer String ergibt einen leeren String.

    Beispiel: ``'one two three'`` wird zu ``'three two one'``.
    """
    return " ".join(reversed(text.split()))
