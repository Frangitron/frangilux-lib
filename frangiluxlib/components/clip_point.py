from enum import auto, StrEnum

from dataclasses import dataclass


class InterpolationMode(StrEnum):
    Linear = auto()
    Step = auto()


@dataclass
class ClipPoint:
    time: float
    value: float
    interpolation_mode: InterpolationMode = InterpolationMode.Linear
