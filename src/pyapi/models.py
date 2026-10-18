from dataclasses import dataclass

@dataclass(frozen=True)
class Change:
    kind:str
    path: str
    old_value: object = None
    new_value: object = None

    def __str__(self)-> str:
        """
        Docstring for __str__

        :param self: Description
        :return: Description
        :rtype: str
        """
        return (
            f"{self.kind}: {self.path} "
            f"(old = {self.old_value!r}, "
            f"new = {self.new_value!r})"
        )