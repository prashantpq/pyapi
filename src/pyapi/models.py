from dataclasses import dataclass

@dataclass(frozen=True)
class Change:
    kind:str
    path: str
    old_value: object = None
    new_value: object = None

    def __str__(self)-> str:
        """
        This magical method will allow to represent the data in format.
        :return: data in format
        :rtype: str
        """
        return (
            f"{self.kind}: {self.path} "
            f"(old = {self.old_value!r}, "
            f"new = {self.new_value!r})"
        )