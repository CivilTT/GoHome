from collections.abc import Callable
from datetime import datetime, timedelta

from returns.result import Result, Success

from common.types.train import InfoLevel, LineInfo, NextTrain, TrainInfo, TrainType

__limit_minute = 10


async def send_next_train(func: Callable[[NextTrain], None]) -> Result[None, Exception]:
  nextTrain = NextTrain(
    departure_time=datetime.now() + timedelta(minutes=10),
    train_name="テスト線",
    train_type=TrainType.LOCAL,
  )

  # フロントエンドに次電車の情報を返す
  func(nextTrain)

  return Success(None)


async def send_train_info(func: Callable[[TrainInfo], None]) -> Result[None, Exception]:
  sampleInfo = TrainInfo(
    level=InfoLevel.CRITICAL,
    train_name="運転障害テスト線",
    title="テスト用の運転障害が発生しました．",
    description="テスト駅で発生した障害により５分の遅延が発生しています．",
  )

  # フロントエンドに運行情報を返す
  func(sampleInfo)

  return Success(None)


async def get_registered_lines() -> Result[list[LineInfo], Exception]:
  lines = [
    LineInfo(line_id=1, line_name="テスト線"),
    LineInfo(line_id=2, line_name="テスト線1"),
    LineInfo(line_id=3, line_name="テスト線2"),
  ]
  return Success(lines)


async def get_limit_minute() -> Result[int, Exception]:
  return Success(__limit_minute)


async def set_limit_minute(minute: int) -> Result[None, Exception]:
  global __limit_minute
  __limit_minute = minute
  return Success(None)
