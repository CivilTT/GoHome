from api.outerlink import OuterLinkApi
from api.timetable import TimetableApi
from api.train import TrainApi
from api.ui import UiApi


class Api:
  def __init__(self, use_mock_api: bool):
    self.Train = TrainApi(use_mock_api)
    self.OuterLink = OuterLinkApi(use_mock_api)
    self.Timetable = TimetableApi(use_mock_api)
    self.Ui = UiApi(use_mock_api)


API = Api(False)
