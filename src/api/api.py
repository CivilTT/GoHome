from pydantic import BaseModel

from api.outerlink import OuterLinkApi
from api.timetable import TimetableApi
from api.train import TrainApi
from api.ui import UiApi

USE_MOCK_API = False


class Api(BaseModel):
  @staticmethod
  def is_using_mock_api() -> bool:
    return USE_MOCK_API

  Train = TrainApi(USE_MOCK_API)
  OuterLink = OuterLinkApi(USE_MOCK_API)
  Timetable = TimetableApi(USE_MOCK_API)
  Ui = UiApi(USE_MOCK_API)


API = Api()
