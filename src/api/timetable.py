from pydantic import BaseModel
from returns.result import Failure, Result

from api.api import USE_MOCK_API
from common.types.timetable import TimeTable, TimetableSetterOptions
from common.types.train import LineId


class TimetableApi(BaseModel):
  @staticmethod
  async def get_timetable(line_id: LineId) -> Result[TimeTable, Exception]:
    if USE_MOCK_API:
      from mocks.timetable import get_timetable

      return get_timetable(line_id)
    else:
      return Failure(NotImplementedError())

  @staticmethod
  async def set_timetable(
    trian_name: str, statin_name: str, bound: str, options: TimetableSetterOptions
  ) -> Result[LineId, Exception]:
    if USE_MOCK_API:
      from mocks.timetable import set_timetable

      return set_timetable(trian_name, statin_name, bound, options)
    else:
      return Failure(NotImplementedError())

  @staticmethod
  async def remove_timetable(line_id: LineId) -> Result[None, Exception]:
    if USE_MOCK_API:
      from mocks.timetable import remove_timetable

      return remove_timetable(line_id)
    else:
      return Failure(NotImplementedError())
