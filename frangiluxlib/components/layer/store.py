import json
import os.path

from frangiluxlib.components.layer.layer import Layer
from frangiluxlib.reactive_channels import ReactiveChannels

from pythonhelpers.reactive import Reactive
from pythonhelpers.singleton_metaclass import SingletonMetaclass


# FIXME is it a singleton ?
class LayerStore(metaclass=SingletonMetaclass):
    _filename = "layers.json"

    def __init__(self):
        self.layers: dict[str, Layer] = {}

    def load(self) -> None:
        if os.path.exists(self._filename):
            with open(self._filename, "r") as f:
                data = json.load(f)
                self.layers = [Layer.from_dict(clip) for clip in data]

        Reactive().notify_observers(
            ReactiveChannels.Layers,
            self.layers
        )

    def save(self) -> None:
        data = [layer.to_dict() for layer in self.layers]
        with open(self._filename, "w") as f:
            json.dump(data, f, indent=2)

    def new(self, layer: Layer) -> None:
        if layer.name in self.layers:
            raise ValueError(f"Layer name {layer.name} already exists")

        self.layers[layer.name] = layer
        Reactive().notify_observers(
            ReactiveChannels.LayersNew,
            layer
        )
