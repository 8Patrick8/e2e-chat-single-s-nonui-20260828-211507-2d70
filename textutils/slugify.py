"""Erzeugung URL-freundlicher Slugs."""


def slugify(text: str) -> str:
    """Erzeuge einen URL-freundlichen Slug aus ``text``.

    Der Text wird in Kleinbuchstaben umgewandelt; jedes Nicht-Alphanumerische
    (``str.isalnum``) wird durch einen Bindestrich ersetzt. Aufeinanderfolgende
    Bindestriche werden zu einem einzelnen zusammengefasst und führende sowie
    abschließende Bindestriche werden entfernt. Ein leerer String ergibt einen
    leeren Slug.
    """
    replaced = "".join(char if char.isalnum() else "-" for char in text.lower())
    return "-".join(part for part in replaced.split("-") if part)
