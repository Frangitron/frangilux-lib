from enum import Enum

from dataclasses import dataclass


class InterpolationMode(Enum):
    Linear = 1
    Step = 2


@dataclass
class ClipPoint:
    time: float
    value: float
    interpolation_mode: InterpolationMode = InterpolationMode.Linear
