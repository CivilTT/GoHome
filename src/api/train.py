from collections.abc import Callable

from pydantic import BaseModel
from returns.result import Failure, Result

from api.api import USE_MOCK_API
from common.types.train import LineInfo, NextTrain, TrainInfo


class TrainApi(BaseModel):
  @staticmethod
  async def send_next_train(
    func: Callable[[NextTrain], None],
  ) -> Result[None, Exception]:
    if USE_MOCK_API:
      from mocks.train import send_next_train

      return send_next_train(func)
    else:
      return Failure(NotImplementedError())

  @staticmethod
  async def send_train_info(
    func: Callable[[TrainInfo], None],
  ) -> Result[None, Exception]:
    if USE_MOCK_API:
      from mocks.train import send_train_info

      return send_train_info(func)
    else:
      return Failure(NotImplementedError())

  @staticmethod
  async def get_registered_lines() -> Result[list[LineInfo], Exception]:
    if USE_MOCK_API:
      from mocks.train import get_registered_lines

      return get_registered_lines()
    else:
      return Failure(NotImplementedError())

  @staticmethod
  async def get_limit_minute() -> Result[int, Exception]:
    """
    「N分以下の電車は表示しない」に該当するNの値を取得する
    """
    if USE_MOCK_API:
      from mocks.train import get_limit_minute

      return get_limit_minute()
    else:
      return Failure(NotImplementedError())

  @staticmethod
  async def set_limit_minute(minute: int) -> Result[None, Exception]:
    """
    「N分以下の電車は表示しない」に該当するNの値を設定する
    """
    if USE_MOCK_API:
      from mocks.train import set_limit_minute

      return set_limit_minute(minute)
    else:
      return Failure(NotImplementedError())
