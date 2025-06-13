from dataclasses import dataclass, field

from frangiluxlib.components.clip_point import ClipPoint
from frangiluxlib.components.time_configuration import TimeConfiguration


@dataclass
class Clip:
    name: str
    time_configuration: TimeConfiguration
    points: list[ClipPoint] = field(default_factory=list)

    def add_point(self, point: ClipPoint):
        self.points.append(point)
        self.sort()

    def sort(self):
        self.points.sort(key=lambda x: x.time)
