from returns.pipeline import is_successful

from common.types.train import NextTrain, TrainInfo
from mocks.train import (
  get_limit_minute,
  get_registered_lines,
  send_next_train,
  send_train_info,
  set_limit_minute,
)


def test_send_next_train():
  """
  次の電車情報の送信をテストします。
  """
  called_with: list[NextTrain] = []

  def mock_func(train: NextTrain):
    called_with.append(train)

  result = send_next_train(mock_func)
  assert is_successful(result)
  assert len(called_with) == 1
  assert isinstance(called_with[0], NextTrain)


def test_send_train_info():
  """
  電車情報の送信をテストします。
  """
  called_with: list[TrainInfo] = []

  def mock_func(info: TrainInfo):
    called_with.append(info)

  result = send_train_info(mock_func)
  assert is_successful(result)
  assert len(called_with) == 1
  assert isinstance(called_with[0], TrainInfo)


def test_get_registered_lines():
  """
  登録済みの路線取得をテストします。
  """
  result = get_registered_lines()
  assert is_successful(result)
  lines = result.unwrap()
  assert isinstance(lines, list)
  assert len(lines) > 0


def test_limit_minute():
  """
  制限時間（分）の取得と設定をテストします。
  """
  # 初期値の取得
  initial_result = get_limit_minute()
  assert is_successful(initial_result)
  initial_minute = initial_result.unwrap()
  assert isinstance(initial_minute, int)

  # 新しい値を設定
  new_minute_value = initial_minute + 5
  set_result = set_limit_minute(new_minute_value)
  assert is_successful(set_result)

  # 新しい値を取得
  new_result = get_limit_minute()
  assert is_successful(new_result)
  new_minute = new_result.unwrap()
  assert new_minute == new_minute_value
