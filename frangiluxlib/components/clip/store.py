import json
import os

from frangiluxlib.components.clip.clip import Clip
from pythonhelpers.singleton_metaclass import SingletonMetaclass


# FIXME is it a singleton ?
class ClipStore(metaclass=SingletonMetaclass):
    _filename = "clips.json"

    def __init__(self):
        self.clips: list[Clip] = []

    def load(self) -> None:
        if os.path.exists(self._filename):
            with open(self._filename, "r") as f:
                data = json.load(f)
                self.clips = [Clip.from_dict(clip) for clip in data]

    def save(self) -> None:
        data = [clip.to_dict() for clip in self.clips]
        with open(self._filename, "w") as f:
            json.dump(data, f, indent=2)
