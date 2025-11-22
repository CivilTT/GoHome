from collections.abc import Callable

from returns.result import Failure, Result

from common.types.api import BaseApi
from common.types.train import LineInfo, NextTrain, TrainInfo


class TrainApi(BaseApi):
  async def send_next_train(
    self,
    func: Callable[[NextTrain], None],
  ) -> Result[None, Exception]:
    if self.use_mock_api:
      from mocks.train import send_next_train

      return await send_next_train(func)
    else:
      return Failure(NotImplementedError())

  async def send_train_info(
    self,
    func: Callable[[TrainInfo], None],
  ) -> Result[None, Exception]:
    if self.use_mock_api:
      from mocks.train import send_train_info

      return await send_train_info(func)
    else:
      return Failure(NotImplementedError())

  async def get_registered_lines(
    self,
  ) -> Result[list[LineInfo], Exception]:
    if self.use_mock_api:
      from mocks.train import get_registered_lines

      return await get_registered_lines()
    else:
      return Failure(NotImplementedError())

  async def get_limit_minute(
    self,
  ) -> Result[int, Exception]:
    """
    「N分以下の電車は表示しない」に該当するNの値を取得する
    """
    if self.use_mock_api:
      from mocks.train import get_limit_minute

      return await get_limit_minute()
    else:
      return Failure(NotImplementedError())

  async def set_limit_minute(self, minute: int) -> Result[None, Exception]:
    """
    「N分以下の電車は表示しない」に該当するNの値を設定する
    """
    if self.use_mock_api:
      from mocks.train import set_limit_minute

      return await set_limit_minute(minute)
    else:
      return Failure(NotImplementedError())
