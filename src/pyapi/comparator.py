from pyapi.models import Change
from pathlib import Path
import json

def _json_type(value: any) -> any:

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

def _compare(old: dict, new: dict, path: str, changes: list)-> list:

    old_type: any = _json_type(old)
    new_type: any = _json_type(new)

    if old_type != new_type:
        changes.append(
            Change(
                kind= "type_changed",
                path= path or "$",
                old_value= old_type,
                new_value= new_type
            )
        )
        return
    
    if isinstance(old, dict):
        old_keys: list = set(old)
        new_keys: list = set(new)

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
        for index, (old_item, new_item) in enumerate(zip(old, new)):
            _compare(
                old_item,
                new_item,
                f"{path}[{index}]",
                changes
            )
    
def json_compare(old: dict, new: dict) -> list:
    old_path: str = Path(old)
    new_path: str = Path(new)

    with old_path.open(encoding="utf-8") as f:
        old_data: dict = json.load(f)
    
    with new_path.open(encoding="utf-8") as f:
        new_data: dict = json.load(f)
    
    changes: list= []
    _compare(
        old_data,
        new_data,
        "$",
        changes
    )
    return changes




        



