from returns.result import Result, Success

from common.types.ui import ShowingComponents

# In-memory store for the showing components
__showing_components = ShowingComponents(
  timetable=True,
  outerlink=True,
  trainInfo=True,
)


def get_showing() -> Result[ShowingComponents, Exception]:
  """
  Mock implementation for getting the showing components.
  """
  return Success(__showing_components)


def set_showing(showing: ShowingComponents) -> Result[None, Exception]:
  """
  Mock implementation for setting the showing components.
  """
  global __showing_components
  __showing_components = showing
  return Success(None)
