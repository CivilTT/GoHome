from pydantic import BaseModel
from returns.result import Failure, Result

from api.api import USE_MOCK_API
from common.types.timetable import TimeTable, TimetableSetterOptions
from common.types.train import LineId


class TimetableApi(BaseModel):
  @staticmethod
  def get_timetable(line_id: LineId) -> Result[TimeTable, Exception]:
    if USE_MOCK_API:
      return Failure(NotImplementedError())
    else:
      return Failure(NotImplementedError())

  @staticmethod
  def set_timetable(
    trian_name: str, statin_name: str, bound: str, options: TimetableSetterOptions
  ) -> Result[LineId, Exception]:
    if USE_MOCK_API:
      return Failure(NotImplementedError())
    else:
      return Failure(NotImplementedError())

  @staticmethod
  def remove_timetable(line_id: LineId) -> Result[None, Exception]:
    if USE_MOCK_API:
      return Failure(NotImplementedError())
    else:
      return Failure(NotImplementedError())
