from returns.pipeline import is_successful

from common.types.train import NextTrain, TrainInfo
from mocks.train import (
    get_limit_minute,
    get_registered_lines,
    send_next_train,
    send_train_info,
    set_limit_minute,
)


def test_send_next_train():
    """
    Test sending next train info.
    """
    called_with: list[NextTrain] = []

    def mock_func(train: NextTrain):
        called_with.append(train)

    result = send_next_train(mock_func)
    assert is_successful(result)
    assert len(called_with) == 1
    assert isinstance(called_with[0], NextTrain)


def test_send_train_info():
    """
    Test sending train info.
    """
    called_with: list[TrainInfo] = []

    def mock_func(info: TrainInfo):
        called_with.append(info)

    result = send_train_info(mock_func)
    assert is_successful(result)
    assert len(called_with) == 1
    assert isinstance(called_with[0], TrainInfo)


def test_get_registered_lines():
    """
    Test getting registered lines.
    """
    result = get_registered_lines()
    assert is_successful(result)
    lines = result.unwrap()
    assert isinstance(lines, list)
    assert len(lines) > 0


def test_limit_minute():
    """
    Test getting and setting the limit minute.
    """
    # Get initial value
    initial_result = get_limit_minute()
    assert is_successful(initial_result)
    initial_minute = initial_result.unwrap()
    assert isinstance(initial_minute, int)

    # Set a new value
    new_minute_value = initial_minute + 5
    set_result = set_limit_minute(new_minute_value)
    assert is_successful(set_result)

    # Get the new value
    new_result = get_limit_minute()
    assert is_successful(new_result)
    new_minute = new_result.unwrap()
    assert new_minute == new_minute_value
