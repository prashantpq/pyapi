
# pyapi-diff

**A lightweight Python library to detect and report changes between JSON structures.**

`pyapi-diff` compares two JSON files and identifies structural, data type, and value changes.

It is useful for detecting changes in API response structures, checking compatibility between API versions, and identifying unexpected changes in JSON data.

## Features

- **Key Addition Detection** — Identifies keys present in the new structure but missing from the old structure.
- **Key Removal Detection** — Identifies keys present in the old structure but missing from the new structure.
- **Type Change Detection** — Detects when a value's data type changes between two structures.
- **Value Change Detection** — Identifies changes in values when their data types remain the same.
- **List Item Addition Detection** — Detects elements added to the end of JSON arrays.
- **List Item Removal Detection** — Detects elements removed from the end of JSON arrays.
- **Nested Structure Comparison** — Recursively detects changes within nested JSON objects and arrays.
- **Readable Change Paths** — Reports the exact location of each detected change using JSON-style paths.
- **Boolean and Number Distinction** — Correctly distinguishes boolean values from numeric values.

## Installation

```bash
pip install pyapi-diff
```

## Quick Start

Create two JSON files: `old.json` and `new.json`.

**old.json**

```json
{
  "id": 101,
  "name": "abc",
  "age": 55,
  "address": {
    "city": "san francisco",
    "pincode": 12345
  },
  "skills": ["Python", "SQL"]
}
```

**new.json**

```json
{
  "id": "101",
  "name": "xyz",
  "contact": 1234567890,
  "address": {
    "city": "Seattle",
    "pincode": 1234
  },
  "skills": ["Python", "SQL"]
}
```

Compare the files using Python:

```python
from pyapi import json_compare

changes = json_compare("old.json", "new.json")

for change in changes:
    print(change)
```

### Output

```text
TYPE_CHANGED: $.id (old = 'number', new = 'string')
KEY_REMOVED: $.age (old = 55, new = None)
KEY_ADDED: $.contact (old = None, new = 1234567890)
VALUE_CHANGED: $.address.city (old = 'san francisco', new = 'Seattle')
VALUE_CHANGED: $.address.pincode (old = 12345, new = 1234)
VALUE_CHANGED: $.name (old = 'abc', new = 'xyz')
```

## Detected Change Types

| Change Type | Description |
|---|---|
| `KEY_ADDED` | A key exists in the new structure but not in the old structure. |
| `KEY_REMOVED` | A key exists in the old structure but not in the new structure. |
| `TYPE_CHANGED` | A value's data type differs between the old and new structures. |
| `VALUE_CHANGED` | A value changes while its data type remains the same. |
| `LIST_ITEM_ADDED` | An element is added to the end of a list. |
| `LIST_ITEM_REMOVED` | An element is removed from the end of a list. |

## How It Works

`pyapi-diff` compares an old JSON structure against a new one and reports detected differences.

For example:

**Old structure**

```json
{
  "user": {
    "id": 101,
    "name": "Alice"
  }
}
```

**New structure**

```json
{
  "user": {
    "id": "101",
    "name": "Bob",
    "email": "alice@example.com"
  }
}
```

The detected changes include:

- `TYPE_CHANGED` at `$.user.id`, because `id` changes from a number to a string.
- `KEY_ADDED` at `$.user.email`, because `email` is newly introduced.
- `VALUE_CHANGED` at `$.user.name`, because `name` changes from `"Alice"` to `"Bob"`.

## Use Cases

- **API Response Comparison** — Identify changes between responses from different API versions.
- **Breaking Change Detection** — Find removed keys or changed data types that could break API consumers.
- **Regression Testing** — Detect unexpected changes in JSON response structures during development.
- **Data Validation** — Check whether incoming JSON data maintains the expected structure.
- **Configuration Comparison** — Identify added, removed, or modified settings.

## Requirements

- Python 3.10 or later

## Development

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd pyapi
```

Install dependencies using [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

Run tests:

```bash
uv run python -m pytest -v
```

## Project Status

`pyapi-diff` is currently in its initial feature release, `0.1.0`.

The library supports detecting JSON structural changes, data type changes, value changes, and list length changes. Additional functionality may be introduced in future releases.

## Contributing

Contributions, bug reports, and feature suggestions are welcome.

Feel free to open an issue or submit a pull request in the project's GitHub repository.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.