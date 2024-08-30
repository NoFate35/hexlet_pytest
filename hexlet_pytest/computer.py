class Computer:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def get_computer_info(self):
        info = []
        for component, i in enumerate(self.components):
            info.append(f":{i}:{component}")
        return info

    def __eq__(self, other):
        if not isinstance(other, Computer):
            return False
        return sorted(self.components) == sorted(other.components)

    def __str__(self):
        return ";".join(c.name for c in self.components)
