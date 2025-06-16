from dataclasses import dataclass, field

from dataclasses_json import dataclass_json

from frangiluxlib.components.clip_point.clip_point import ClipPoint
from frangiluxlib.components.time_configuration import TimeConfiguration


@dataclass_json
@dataclass
class Clip:
    name: str
    time_configuration: TimeConfiguration
    _points: list[ClipPoint] = field(default_factory=list)
    play_position: float = 0.0

    def add_point(self, point: ClipPoint):
        self._points.append(point)
        self.sort()

    def points(self) -> list[ClipPoint]:
        return [point for point in self._points if point.time <= self.time_configuration.duration]

    def remove_point(self, point: ClipPoint):
        self._points.remove(point)

    def sort(self):
        self._points.sort(key=lambda x: x.time)
