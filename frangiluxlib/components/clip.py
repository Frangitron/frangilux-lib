from dataclasses import dataclass, field

from dataclasses_json import dataclass_json

from frangiluxlib.components.clip_point import ClipPoint
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

    def play_value(self) -> float | None:
        points = self.points()
        if not points:
            return None

        # TODO do we want that ?
        time = self.play_position % self.time_configuration.duration if self.play_position != self.time_configuration.duration else self.play_position

        if time <= points[0].time:
            return points[0].value

        for i in range(len(points) - 1):
            if points[i].time <= time <= points[i + 1].time:
                return points[i].value + (points[i + 1].value - points[i].value) * (time - points[i].time) / (points[i + 1].time - points[i].time)

        return points[-1].value
