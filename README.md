# textutils

Kleine, eigenständige Python-Bibliothek mit fünf einfachen, unabhängigen
String-Hilfsfunktionen: `slugify`, `truncate`, `word_count`, `is_palindrome` und
`reverse_words`. Reine Backend-Bibliothek ohne UI und ohne externe
Abhängigkeiten (nur Standardbibliothek).

## Tech-Stack

- Sprache: Python 3.10+
- Testing: pytest
- Packaging: pyproject.toml (setuptools)
- Abhängigkeiten: keine (nur Standardbibliothek)

## Installation

```bash
pip install -e .
```

## Tests

```bash
pytest
```

## Verwendung

Alle fünf Funktionen werden aus dem Paket re-exportiert und sind per
`from textutils import ...` importierbar:

| Funktion         | Signatur                          | Verhalten                                                                                      |
| ---------------- | --------------------------------- | ---------------------------------------------------------------------------------------------- |
| `slugify`        | `slugify(text: str) -> str`       | Erzeugt einen URL-freundlichen Slug, z. B. `'Hello, World!'` -> `'hello-world'`.               |
| `truncate`       | `truncate(text, max_len) -> str`  | Kürzt auf höchstens `max_len` Zeichen; bei Kürzung endet das Ergebnis mit `…` (U+2026). `max_len < 1` wirft `ValueError`. |
| `word_count`     | `word_count(text: str) -> int`    | Zählt Wörter, ignoriert Mehrfach-Leerzeichen, leerer String ergibt `0`.                        |
| `is_palindrome`  | `is_palindrome(text: str) -> bool`| Prüft auf Palindrom; ignoriert Groß-/Kleinschreibung und Satzzeichen.                          |
| `reverse_words`  | `reverse_words(text: str) -> str` | Dreht die Wortreihenfolge um, z. B. `'one two three'` -> `'three two one'`.                     |

Beispiel:

```python
from textutils import slugify, word_count

slugify("Hello, World!")  # 'hello-world'
word_count("a  b   c")  # 3
```

## Features

- Installierbares Paket (`pip install -e .`)
- Fünf String-Hilfsfunktionen mit vollständig typisierten Signaturen
- Keine externen Abhängigkeiten, nur Standardbibliothek

Hinweis: In diesem Stand sind die fünf Funktionen als Stubs angelegt; die
Implementierung folgt in späteren Tickets.
