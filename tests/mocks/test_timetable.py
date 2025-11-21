from returns.pipeline import is_successful

from common.types.timetable import TimetableSetterOptions
from mocks.timetable import get_timetable, remove_timetable, set_timetable


def test_get_timetable():
    """
    Test getting a timetable.
    """
    # Test getting an existing timetable
    timetable_result = get_timetable(1)
    assert is_successful(timetable_result)
    timetable = timetable_result.unwrap()
    assert timetable is not None
    assert len(timetable.items) > 0

    # Test getting a non-existing timetable
    timetable_result = get_timetable(999)
    assert is_successful(timetable_result)
    timetable = timetable_result.unwrap()
    assert timetable is not None
    assert len(timetable.items) == 0


def test_set_timetable():
    """
    Test setting a new timetable.
    """
    options = TimetableSetterOptions(
        enable_local=True, enable_rapid=False, enable_express=False
    )
    result = set_timetable("New Line", "New Station", "New Bound", options)
    assert is_successful(result)
    new_line_id = result.unwrap()

    timetable_result = get_timetable(new_line_id)
    assert is_successful(timetable_result)
    timetable = timetable_result.unwrap()
    assert timetable is not None
    assert len(timetable.items) > 0


def test_remove_timetable():
    """
    Test removing a timetable.
    """
    # First, add a timetable to remove
    options = TimetableSetterOptions()
    add_result = set_timetable("To Remove", "Station", "Bound", options)
    new_line_id = add_result.unwrap()

    # Test that it exists
    assert is_successful(get_timetable(new_line_id))

    # Now, remove it
    remove_result = remove_timetable(new_line_id)
    assert is_successful(remove_result)

    # Test that it's gone
    timetable_result = get_timetable(new_line_id)
    timetable = timetable_result.unwrap()
    assert len(timetable.items) == 0
