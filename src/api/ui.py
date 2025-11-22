from returns.result import Failure, Result

from common.types.api import BaseApi
from common.types.ui import ShowingComponents


class UiApi(BaseApi):
  async def get_showing(self) -> Result[ShowingComponents, Exception]:
    if self.use_mock_api:
      from mocks.ui import get_showing

      return await get_showing()
    else:
      return Failure(NotImplementedError())

  async def set_showing(self, showing: ShowingComponents) -> Result[None, Exception]:
    if self.use_mock_api:
      from mocks.ui import set_showing

      return await set_showing(showing)
    else:
      return Failure(NotImplementedError())
