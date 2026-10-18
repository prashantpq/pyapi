from pyapi.comparator import json_compare

changes = json_compare('tests/old.json', 'tests/new.json')

for change in changes:
    print(change)