
import json

from pyapi import json_compare


def run_comparison(tmp_path, old_data, new_data):
    """Write JSON files and return the detected changes."""
    old_file = tmp_path / "old.json"
    new_file = tmp_path / "new.json"

    old_file.write_text(
        json.dumps(old_data),
        encoding="utf-8",
    )
    new_file.write_text(
        json.dumps(new_data),
        encoding="utf-8",
    )

    return json_compare(str(old_file), str(new_file))


def test_detects_removed_key(tmp_path):
    old = {"name": "Alice", "age": 55}
    new = {"name": "Bob"}

    changes = run_comparison(tmp_path, old, new)

    assert len(changes) == 1
    assert changes[0].kind == "KEY_REMOVED"
    assert changes[0].path == "$.age"
    assert changes[0].old_value == 55


def test_detects_added_key(tmp_path):
    old = {"name": "Alice"}
    new = {"name": "Bob", "contact": 1234567890}

    changes = run_comparison(tmp_path, old, new)

    assert len(changes) == 1
    assert changes[0].kind == "KEY_ADDED"
    assert changes[0].path == "$.contact"
    assert changes[0].new_value == 1234567890


def test_detects_type_change(tmp_path):
    old = {"id": 101}
    new = {"id": "101"}

    changes = run_comparison(tmp_path, old, new)

    assert len(changes) == 1
    assert changes[0].kind == "TYPE_CHANGED"
    assert changes[0].path == "$.id"
    assert changes[0].old_value == "number"
    assert changes[0].new_value == "string"


def test_ignores_string_value_change(tmp_path):
    old = {"name": "Alice"}
    new = {"name": "Bob"}

    changes = run_comparison(tmp_path, old, new)

    assert changes == ["Both json are identical"]


def test_ignores_numeric_value_change(tmp_path):
    old = {"age": 25}
    new = {"age": 55}

    changes = run_comparison(tmp_path, old, new)

    assert changes == ["Both json are identical"]


def test_detects_nested_added_key(tmp_path):
    old = {"user": {"name": "Alice"}}
    new = {"user": {"name": "Bob", "email": "alice@example.com"}}

    changes = run_comparison(tmp_path, old, new)

    assert len(changes) == 1
    assert changes[0].kind == "KEY_ADDED"
    assert changes[0].path == "$.user.email"


def test_detects_multiple_changes_and_ignores_value_changes(tmp_path):
    old = {
        "id": 101,
        "age": 55,
        "name": "Alice",
    }
    new = {
        "id": "101",
        "name": "Bob",
        "contact": 1234567890,
    }

    changes = run_comparison(tmp_path, old, new)

    actual = {(change.kind, change.path) for change in changes}

    expected = {
        ("KEY_REMOVED", "$.age"),
        ("KEY_ADDED", "$.contact"),
        ("TYPE_CHANGED", "$.id"),
    }

    assert actual == expected
    assert ("key_removed", "$.name") not in actual


def test_identical_json_structures(tmp_path):
    data = {
        "id": 101,
        "name": "Alice",
        "profile": {"city": "Mumbai"},
    }

    changes = run_comparison(tmp_path, data, data)

    assert changes == ["Both json are identical"]


def test_detects_type_change_inside_list(tmp_path):
    old = {"items": [101]}
    new = {"items": ["101"]}

    changes = run_comparison(tmp_path, old, new)

    assert len(changes) == 1
    assert changes[0].kind == "TYPE_CHANGED"
    assert changes[0].path == "$.items[0]"
    assert changes[0].old_value == "number"
    assert changes[0].new_value == "string"


def test_distinguishes_boolean_from_number(tmp_path):
    old = {"active": True}
    new = {"active": 1}

    changes = run_comparison(tmp_path, old, new)

    assert len(changes) == 1
    assert changes[0].kind == "TYPE_CHANGED"
    assert changes[0].path == "$.active"
    assert changes[0].old_value == "boolean"
    assert changes[0].new_value == "number"