from dataclasses import dataclass, field


@dataclass(order=True)
class Component:
    sort_index: str = field(init=False, repr=False)
    name: str

    def __post_init__(self):
        self.sort_index = self.name


motherboard = Component("motherboard")
power_supply = Component("power_supply")
processor = Component("processor")
memory = Component("memory")
storage = Component("storage")
graphics_card = Component("graphics_card")
