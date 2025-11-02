from pydantic import BaseModel

from common.types.train import TrainType


class TimetableSetterOptions(BaseModel):
  """
  時刻表設定オプション

  @param enable_local: 各駅停車を有効にするかどうか
  @param enable_rapid: 快速を有効にするかどうか
  @param enable_express: 有料特急を有効にするかどうか
  @param showing_bounds: 表示する行き先のリスト
  @param disable_bounds: 非表示にする行き先のリスト
  """

  enable_local: bool = True
  enable_rapid: bool = True
  enable_express: bool = True
  showing_bounds: list[str] = []
  disable_bounds: list[str] = []


class TimeTableItem(BaseModel):
  """
  時刻表の各電車

  @param hour: 出発時の時(hour)
  @param minute: 出発時の分(minute)
  @param train_type: 電車の種別
  """

  hour: int
  minute: int
  train_type: TrainType


class TimeTable(BaseModel):
  """
  時刻表

  @param items: 各電車のリスト
  """

  items: list[TimeTableItem]
