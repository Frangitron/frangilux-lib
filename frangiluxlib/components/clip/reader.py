from frangiluxlib.components.clip.clip import Clip
from frangiluxlib.components.clip_point.clip_point import ClipPoint
from frangiluxlib.components.clip_point.reference_store import ClipPointReferenceStore

from pythonhelpers.singleton_metaclass import SingletonMetaclass


# FIXME make a singleton with an instance of this as a member
class ClipReader(metaclass=SingletonMetaclass):

    def __init__(self):
        self._reference_store = ClipPointReferenceStore()

    def point_value(self, point: ClipPoint) -> float:
        if point.is_reference:
            return self._reference_store.get(point)

        return point.value

    def play_value(self, clip: Clip) -> float | None:
        points = clip.points()
        if not points:
            return None

        # TODO do we want that ?
        if clip.play_position != clip.time_configuration.duration:
            time = clip.play_position % clip.time_configuration.duration
        else:
            time = clip.play_position

        if time <= points[0].time:
            return self.point_value(points[0])

        for i in range(len(points) - 1):
            if points[i].time <= time <= points[i + 1].time:
                value = self.point_value(points[i])
                value1 = self.point_value(points[i + 1])
                return value + (value1 - value) * (time - points[i].time) / (points[i + 1].time - points[i].time)

        return self.point_value(points[-1])
