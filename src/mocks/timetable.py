from returns.result import Failure, Result, Success

from common.types.timetable import (
  TimeTable,
  TimeTableItem,
  TimetableSetterOptions,
)
from common.types.train import LineId, TrainType

# 時刻表のインメモリストア
_timetables: dict[LineId, TimeTable] = {
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


async def get_timetable(line_id: LineId) -> Result[TimeTable, Exception]:
  """
  時刻表を取得するためのモック実装
  """
  if line_id in _timetables:
    return Success(_timetables[line_id].model_copy())
  else:
    # 見つからない場合は、デフォルトまたは空の時刻表を返す
    return Failure(ValueError(f"Timetable (lineID={line_id}) does not found."))


async def set_timetable(
  train_name: str, station_name: str, bound: str, options: TimetableSetterOptions
) -> Result[LineId, Exception]:
  """
  時刻表を設定するためのモック実装
  このモックはオプションに基づいてサンプルの時刻表を生成します。
  train_name, station_name, bound パラメータはこのモックでは無視されます。
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
  new_id = max(_timetables.keys()) + 1 if _timetables else 1
  _timetables[new_id] = new_timetable
  return Success(new_id)


async def remove_timetable(line_id: LineId) -> Result[None, Exception]:
  """
  時刻表を削除するためのモック実装
  """
  if line_id in _timetables:
    del _timetables[line_id]
  return Success(None)
