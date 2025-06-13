from dataclasses import dataclass
from enum import Enum


class TimeConfigurationMode(Enum):
    Milliseconds = 1
    Tempo = 2


@dataclass
class TimeConfiguration:
    duration: float
    mode: TimeConfigurationMode
