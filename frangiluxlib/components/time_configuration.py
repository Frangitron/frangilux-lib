from dataclasses import dataclass
from enum import auto, StrEnum


class TimeConfigurationMode(StrEnum):
    Milliseconds = auto()
    Tempo = auto()


@dataclass
class TimeConfiguration:
    duration: float
    mode: TimeConfigurationMode
