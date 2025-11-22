from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class TrainType(str, Enum):
  LOCAL = "local"
  RAPID = "rapid"
  EXPRESS = "express"


class InfoLevel(str, Enum):
  NORMAL = "normal"
  WARNING = "warning"
  CRITICAL = "critical"


LineId = int


class LineInfo(BaseModel):
  """
  電車の路線情報

  @param line_id: 登録時のID
  @param line_name: 電車の線名
  """

  line_id: LineId
  line_name: str


class NextTrain(BaseModel):
  """
  現在時刻から直近で出発する電車の情報

  @param departure_time: 電車の出発時刻
  @param train_name: 電車の線名
  @param train_type: 電車の種別
  """

  departure_time: datetime
  train_name: str
  train_type: TrainType


class TrainInfo(BaseModel):
  """
  電車の運行情報

  @param level: 情報の重要度
  @param train_name: 電車の線名
  @param title: 情報のタイトル
  @param description: 情報の詳細説明
  """

  level: InfoLevel
  train_name: str
  title: str
  description: str
