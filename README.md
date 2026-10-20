# pyapi

**A lightweight Python library to detect structural changes in JSON data.**

`pyapi` compares two JSON-compatible data structures and identifies changes in their structure and data types, without reporting ordinary value changes.

It is useful for detecting changes in API response structures, checking compatibility between API versions, and identifying unexpected changes in JSON data.

## Features

- **Key Addition Detection** — Identifies keys present in the new structure but missing from the old structure.
- **Key Removal Detection** — Identifies keys present in the old structure but missing from the new structure.
- **Type Change Detection** — Detects when a value's data type changes between two structures.
- **Nested Structure Comparison** — Detects structural changes within nested JSON objects.
- **Value-Agnostic Comparison** — Ignores changes to values when their data types remain the same.
- **Readable Change Paths** — Reports the location of each detected change using JSON-style paths.

## Installation

```bash
pip install pyapi-diff
```

## Quick Start

```python
from pyapi import json_compare

old = {
  "id": 101,
  "name": "abc",
  "age": 55,
  "address": {
    "city": "san francisco",
    "pincode": 12345
  },
  "skills": ["Python", "SQL"]
}

new = {
  "id": "101",
  "name": "xyz",
  "contact": 1234567890,
  "address": {
    "city": "Seattle",
    "pincode": 1234
  },
  "skills": ["Python", "SQL"]
}

json_compare(old, new)
```

### Output

```text
key_removed: $.age (old = 55, new = None)
key_added: $.contact (old = None, new = 1234567890)
type_changed: $.id (old = 'number', new = 'string')
```

## Detected Change Types

| Change Type | Description |
|---|---|
| `key_added` | A key exists in the new structure but not in the old structure. |
| `key_removed` | A key exists in the old structure but not in the new structure. |
| `type_changed` | A value's data type differs between the old and new structures. |

## How It Works

`pyapi` compares an old JSON-compatible structure against a new one and reports structural differences.

For example, consider these two objects:

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

- `type_changed` at `$.user.id`, because `id` changes from a number to a string.
- `key_added` at `$.user.email`, because `email` is newly introduced.

The change from `"Alice"` to `"Bob"` is ignored because the value remains a string.

## Use Cases

- **API Response Comparison:** Identify structural changes between responses from different API versions.
- **Breaking Change Detection:** Find removed keys or changed data types that could break API consumers.
- **Regression Testing:** Detect unexpected changes in JSON response structures during development.
- **Data Validation:** Check whether incoming JSON data maintains the expected structure.
- **Configuration Comparison:** Identify added or removed settings and changes in their data types.

## Requirements

- Python 3.10 or later

## Development

Clone the repository:

```bash
git clone https://github.com/prashantpq/pyapi.git
cd pyapi
```

Install dependencies using [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

Run the example or test script:

```bash
uv run python tests/test1.py
```

## Project Status

`pyapi` is currently in its initial release, `0.0.2`.

The current focus is on detecting JSON structural and data type changes. Additional functionality may be introduced in future releases.

## Contributing

Contributions, bug reports, and feature suggestions are welcome.

Feel free to open an issue or submit a pull request in the project's GitHub repository.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.