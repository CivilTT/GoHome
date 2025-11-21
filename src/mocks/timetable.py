from returns.result import Result, Success

from common.types.timetable import (
  TimeTable,
  TimeTableItem,
  TimetableSetterOptions,
)
from common.types.train import LineId, TrainType

# In-memory store for timetables
__timetables: dict[LineId, TimeTable] = {
  1: TimeTable(
    items=[
      TimeTableItem(hour=h, minute=m, train_type=TrainType.LOCAL)
      for h in range(9, 18)
      for m in [0, 15, 30, 45]
    ]
    + [
      TimeTableItem(hour=h, minute=m, train_type=TrainType.RAPID)
      for h in range(9, 18)
      for m in [10, 40]
    ]
  )
}


def get_timetable(line_id: LineId) -> Result[TimeTable, Exception]:
  """
  Mock implementation for getting a timetable.
  """
  if line_id in __timetables:
    return Success(__timetables[line_id])
  else:
    # Return a default or empty timetable if not found
    return Success(TimeTable(items=[]))


def set_timetable(
  train_name: str, station_name: str, bound: str, options: TimetableSetterOptions
) -> Result[LineId, Exception]:
  """
  Mock implementation for setting a timetable.
  This mock will generate a sample timetable based on the options.
  The train_name, station_name, and bound parameters are ignored in this mock.
  """
  items = []
  if options.enable_local:
    items.extend(
      [
        TimeTableItem(hour=h, minute=m, train_type=TrainType.LOCAL)
        for h in range(9, 18)
        for m in [5, 25, 35, 55]
      ]
    )
  if options.enable_rapid:
    items.extend(
      [
        TimeTableItem(hour=h, minute=m, train_type=TrainType.RAPID)
        for h in range(9, 18)
        for m in [20, 50]
      ]
    )
  if options.enable_express:
    items.extend(
      [
        TimeTableItem(hour=h, minute=m, train_type=TrainType.EXPRESS)
        for h in range(10, 17)
        for m in [0]
      ]
    )

  new_timetable = TimeTable(items=items)
  new_id = max(__timetables.keys()) + 1 if __timetables else 1
  __timetables[new_id] = new_timetable
  return Success(new_id)


def remove_timetable(line_id: LineId) -> Result[None, Exception]:
  """
  Mock implementation for removing a timetable.
  """
  if line_id in __timetables:
    del __timetables[line_id]
  return Success(None)
