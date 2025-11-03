from pydantic import BaseModel
from returns.result import Result

from common.types.timetable import TimeTable, TimetableSetterOptions
from common.types.train import LineId


class TimetableApi(BaseModel):
  def __init__(self, is_mock_api: bool):
    super().__init__()
    self.is_mock_api = is_mock_api

  @staticmethod
  def get_timetable(line_id: LineId) -> Result[TimeTable]:
    pass

  @staticmethod
  def set_timetable(
    trian_name: str, statin_name: str, bound: str, options: TimetableSetterOptions
  ) -> Result[LineId]:
    pass

  @staticmethod
  def remove_timetable(line_id: LineId) -> Result[None]:
    pass
