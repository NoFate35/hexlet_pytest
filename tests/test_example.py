from hexlet_pytest.components import motherboard, power_supply, processor, memory, graphics_card, storage
from hexlet_pytest.example import ComputerBuilder, ComputerDirector
from hexlet_pytest.computer import Computer


def test_builder():
    builder = ComputerBuilder()
    base = builder.pre_assemble(motherboard, power_supply)
    assert isinstance(base, ComputerBuilder)

    computer = base.add_processor(processor).get_computer()
    assert isinstance(computer, Computer)


def test_director():
    builder = ComputerBuilder()
    director = ComputerDirector(builder)
    director.build_basic_computer()
    basic_computer = builder.get_computer()

    builder2 = ComputerBuilder()
    basic_computer2 = builder2.pre_assemble(motherboard, power_supply) \
        .add_processor(processor) \
        .add_memory(memory) \
        .add_storage(storage) \
        .get_computer()

    assert basic_computer == basic_computer2

    gaming_computer = director.build_gaming_computer()
    gaming_computer = builder.get_computer()
    gaming_computer_2 = builder2.pre_assemble(motherboard, power_supply) \
        .add_processor(processor) \
        .add_memory(memory) \
        .add_storage(storage) \
        .add_graphics_card(graphics_card) \
        .get_computer()

    assert gaming_computer == gaming_computer_2

    director.build_server_computer()
    server_computer = builder.get_computer()
    server_computer_2 = builder2.pre_assemble(motherboard, power_supply) \
        .add_processor(processor) \
        .add_memory(memory) \
        .add_storage(storage) \
        .add_processor(processor) \
        .add_memory(memory) \
        .get_computer()

    assert server_computer == server_computer_2
