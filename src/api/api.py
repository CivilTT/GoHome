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

  Train = TrainApi()
  OuterLink = OuterLinkApi()
  Timetable = TimetableApi()
  Ui = UiApi()


API = Api()
