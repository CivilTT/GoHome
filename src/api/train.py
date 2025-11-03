from typing import Callable

from pydantic import BaseModel
from returns.result import Result

from common.types.train import LineInfo, NextTrain, TrainInfo


class TrainApi(BaseModel):
  def __init__(self, is_mock_api: bool):
    super().__init__()
    self.is_mock_api = is_mock_api

  @staticmethod
  def send_next_train(func: Callable[[NextTrain], None]) -> Result[None]:
    # Importしてきた実装を挿入する
    pass

  @staticmethod
  def send_train_info(func: Callable[[TrainInfo], None]) -> Result[None]:
    pass

  @staticmethod
  def get_registered_lines() -> Result[list[LineInfo]]:
    pass

  @staticmethod
  def get_limit_minute() -> Result[int]:
    """
    「N分以下の電車は表示しない」に該当するNの値を取得する
    """
    pass

  @staticmethod
  def set_limit_minute(minute: int) -> Result[None]:
    """
    「N分以下の電車は表示しない」に該当するNの値を設定する
    """
    pass
