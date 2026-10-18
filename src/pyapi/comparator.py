from pyapi.models import Change
from pathlib import Path

def _json_type(value):
    """

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

# def _compare(old: str, new: str, path: str, changes: list):
#     """
#     Docstring for _compare
    
#     :param old: Description
#     :type old: str
#     :param new: Description
#     :type new: str
#     :param path: Description
#     :type path: str
#     :param changes: Description
#     :type changes: list
#     """
#     old_type = _json_type(old)
#     new_type = _json_type(new)



