import json

from frangiluxlib.components.clip_point import ClipPoint
from pythonhelpers.singleton_metaclass import SingletonMetaclass


# TODO make abstract ? Separate store/loader or rename ?
# FIXME use a Singleton to hold one instance
class ClipPointReferenceStore(metaclass=SingletonMetaclass):

    def __init__(self):
        self.references: dict[str, float] = {}

    def references_names(self) -> list[str]:
        return list(self.references.keys())

    def load(self) -> None:
        with open("references.json", "r") as f:
            self.references = json.load(f)

    def save(self) -> None:
        with open("references.json", "w") as f:
            json.dump(self.references, f, indent=2)

    def get(self, point: ClipPoint) -> float:
        if point.reference_name not in self.references:
            if point.reference_name is None:
                return point.value

            self.references[point.reference_name] = point.value
            return point.value

        return self.references[point.reference_name]

    def set(self, point: ClipPoint, value: float) -> None:
        if point.reference_name is None:
            raise ValueError("Reference name is None")

        self.references[point.reference_name] = value

    def new(self, name: str, point: ClipPoint) -> None:
        if name in self.references:
            raise ValueError(f"Reference name {name} already exists")

        self.references[name] = point.value
