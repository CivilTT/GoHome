from pydantic import BaseModel
from returns.result import Result

from common.types.ui import ShowingComponents


class UiApi(BaseModel):
  def __init__(self, is_mock_api: bool):
    super().__init__()
    self.is_mock_api = is_mock_api

  @staticmethod
  def get_showing() -> Result[ShowingComponents]:
    pass

  @staticmethod
  def set_showing(showing: ShowingComponents) -> Result[None]:
    pass
