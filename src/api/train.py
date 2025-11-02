from typing import Callable

from pydantic import BaseModel

from common.types.train import LineInfo, NextTrain, TrainInfo


# TODO: Result型でラップする
class TrainApi(BaseModel):
  def __init__(self, is_mock_api: bool):
    super().__init__()
    self.is_mock_api = is_mock_api

  @staticmethod
  def send_next_train(func: Callable[[NextTrain], None]) -> None:
    # Importしてきた実装を挿入する
    pass

  @staticmethod
  def send_train_info(func: Callable[[TrainInfo], None]) -> None:
    pass

  @staticmethod
  def get_registered_lines() -> list[LineInfo]:
    pass

  @staticmethod
  def get_limit_minute() -> int:
    """
    「N分以下の電車は表示しない」に該当するNの値を取得する
    """
    pass

  @staticmethod
  def set_limit_minute(minute: int) -> None:
    """
    「N分以下の電車は表示しない」に該当するNの値を設定する
    """
    pass
