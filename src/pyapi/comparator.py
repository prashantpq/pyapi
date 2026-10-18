from pyapi.models import Change
from pathlib import Path
import json

def _json_type(value):
    """
    Docstring for _json_type
    
    :param value: any datatype
    :type value: Any
    :return: understandable datatype
    :rtype: Any
    """
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, dict):
        return "object"
    if isinstance(value, list):
        return "array"
    return "Unknown"

def _compare(old: str, new: str, path: str, changes: list):
    """
    Docstring for _compare
    
    :param old: Description
    :type old: str
    :param new: Description
    :type new: str
    :param path: Description
    :type path: str
    :param changes: Description
    :type changes: list
    """
    old_type = _json_type(old)
    new_type = _json_type(new)

    if old_type != new_type:
        changes.append(
            Change(
                kind= "type_changes",
                path= path or "$",
                old_value= old_type,
                new_value= new_type
            )
        )
        return
    
    if isinstance(old, dict):
        old_keys = set(old)
        new_keys = set(new)

        for key in sorted(old_keys - new_keys):
            changes.append(
                Change(
                    kind="key_removed",
                    path= f"{path}.{key}",
                    old_value=old[key]
                )
            )
        
        for key in sorted(new_keys - old_keys):
            changes.append(
                Change(
                    kind= "key_added",
                    path= f"{path}.{key}",
                    new_value= new[key]
                )
            )
        
        for key in sorted(old_keys & new_keys):
            _compare(
                old[key],
                new[key],
                f"{path}.{key}",
                changes
            )

    elif isinstance(old, list):
        for index, (old_item, new_item) in zip(old, new):
            _compare(
                old_item,
                new_item,
                f"{path}[{index}]",
                changes
            )
    
    def json_compare(old: str, new: str) -> list:
        old_path = Path(old)
        new_path = Path(new)

        with old_path.open(encoding="utf-8") as f:
            old_data = json.load(f)
        
        with new_path.open(encoding="utf-8") as f:
            new_data = json.load(f)
        
        changes = []
        _compare(
            old_data,
            new_data,
            "$",
            changes
        )
        return changes




        



