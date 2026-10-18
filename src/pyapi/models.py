from dataclasses import dataclass

@dataclass
class Change:
    kind:str
    path: str
    old_value: object = None
    new_value: object = None

    def __str__(self)-> str:
        return (
            f"{self.kind}: {self.path} "
            f"(old = {self.old_value!r}, "
            f"new = {self.new_value!r})"
        )