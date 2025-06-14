import json

from frangiluxlib.components.clip import Clip


# TODO make abstract ? Separate store/loader or rename ?
class ClipStore:

    def __init__(self):
        self.clips: list[Clip] = []

    def load(self) -> None:
        with open("clips.json", "r") as f:
            data = json.load(f)
            self.clips = [Clip.from_dict(clip) for clip in data]

    def save(self) -> None:
        data = [clip.to_dict() for clip in self.clips]
        with open("clips.json", "w") as f:
            json.dump(data, f, indent=2)
