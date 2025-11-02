from pydantic import BaseModel

from common.types.ui import ShowingComponents


# TODO: Result型でラップする
class UiApi(BaseModel):
  def __init__(self, is_mock_api: bool):
    super().__init__()
    self.is_mock_api = is_mock_api

  @staticmethod
  def get_showing() -> ShowingComponents:
    pass

  @staticmethod
  def set_showing(showing: ShowingComponents) -> None:
    pass
