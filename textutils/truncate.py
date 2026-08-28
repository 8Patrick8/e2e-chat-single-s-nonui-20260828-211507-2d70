"""Kürzung von Strings auf eine maximale Länge."""


def truncate(text: str, max_len: int) -> str:
    """Kürze ``text`` auf höchstens ``max_len`` Zeichen.

    Bei Kürzung endet das Ergebnis mit ``…`` (U+2026), die Gesamtlänge
    überschreitet ``max_len`` nie. ``max_len < 1`` wirft einen ``ValueError``.
    """
    raise NotImplementedError
