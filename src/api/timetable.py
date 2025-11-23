from returns.result import Failure, Result

from common.types.api import BaseApi
from common.types.timetable import TimeTable, TimetableSetterOptions
from common.types.train import LineId


class TimetableApi(BaseApi):
  async def get_timetable(self, line_id: LineId) -> Result[TimeTable, Exception]:
    if self.use_mock_api:
      from mocks.timetable import get_timetable

      return await get_timetable(line_id)
    else:
      return Failure(NotImplementedError())

  async def set_timetable(
    self,
    train_name: str,
    station_name: str,
    bound: str,
    options: TimetableSetterOptions,
  ) -> Result[LineId, Exception]:
    if self.use_mock_api:
      from mocks.timetable import set_timetable

      return await set_timetable(train_name, station_name, bound, options)
    else:
      return Failure(NotImplementedError())

  async def remove_timetable(self, line_id: LineId) -> Result[None, Exception]:
    if self.use_mock_api:
      from mocks.timetable import remove_timetable

      return await remove_timetable(line_id)
    else:
      return Failure(NotImplementedError())
