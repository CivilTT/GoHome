from pydantic import BaseModel
from returns.result import Failure, Result

from api.api import USE_MOCK_API
from common.types.ui import ShowingComponents


class UiApi(BaseModel):
  @staticmethod
  def get_showing() -> Result[ShowingComponents, Exception]:
    if USE_MOCK_API:
      return Failure(NotImplementedError())
    else:
      return Failure(NotImplementedError())

  @staticmethod
  def set_showing(showing: ShowingComponents) -> Result[None, Exception]:
    if USE_MOCK_API:
      return Failure(NotImplementedError())
    else:
      return Failure(NotImplementedError())
