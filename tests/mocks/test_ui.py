from returns.pipeline import is_successful

from common.types.ui import ShowingComponents
from mocks.ui import get_showing, set_showing


def test_get_showing():
  """
  Test getting the showing components.
  """
  result = get_showing()
  assert is_successful(result)
  components = result.unwrap()
  assert isinstance(components, ShowingComponents)


def test_set_showing():
  """
  Test setting the showing components.
  """
  # Get initial components
  initial_components = get_showing().unwrap()

  # Create new components state
  new_components_state = ShowingComponents(
    trainInfo=not initial_components.trainInfo,
    timetable=not initial_components.timetable,
    outerlink=not initial_components.outerlink,
  )

  # Set the new state
  set_result = set_showing(new_components_state)
  assert is_successful(set_result)

  # Get the updated state
  updated_components_result = get_showing()
  assert is_successful(updated_components_result)
  updated_components = updated_components_result.unwrap()

  # Check if the state was updated
  assert updated_components.trainInfo == new_components_state.trainInfo
  assert updated_components.timetable == new_components_state.timetable
  assert updated_components.outerlink == new_components_state.outerlink
