from dataclasses import dataclass, field

from dataclasses_json import dataclass_json

from frangiluxlib.components.clip.clip import Clip


@dataclass_json
@dataclass
class Layer:
    name: str
    clips: list[Clip] = field(default_factory=list)
