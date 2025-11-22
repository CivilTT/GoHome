import pytest
from returns.pipeline import is_successful

from api.api import Api
from common.types.timetable import TimetableSetterOptions

TEST_API = Api(True)


@pytest.mark.asyncio
async def test_get_timetable():
  """
  時刻表の取得をテストします。
  """
  # 既存の時刻表の取得をテスト
  timetable_result = await TEST_API.Timetable.get_timetable(1)
  assert is_successful(timetable_result)
  timetable = timetable_result.unwrap()
  assert timetable is not None
  assert len(timetable.items) > 0

  # 存在しない時刻表の取得をテスト
  timetable_result = await TEST_API.Timetable.get_timetable(999)
  assert is_successful(timetable_result)
  timetable = timetable_result.unwrap()
  assert timetable is not None
  assert len(timetable.items) == 0


@pytest.mark.asyncio
async def test_set_timetable():
  """
  新しい時刻表の設定をテストします。
  """
  options = TimetableSetterOptions(
    enable_local=True, enable_rapid=False, enable_express=False
  )
  result = await TEST_API.Timetable.set_timetable(
    "New Line", "New Station", "New Bound", options
  )
  assert is_successful(result)
  new_line_id = result.unwrap()

  timetable_result = await TEST_API.Timetable.get_timetable(new_line_id)
  assert is_successful(timetable_result)
  timetable = timetable_result.unwrap()
  assert timetable is not None
  assert len(timetable.items) > 0


@pytest.mark.asyncio
async def test_remove_timetable():
  """
  時刻表の削除をテストします。
  """
  # まず、削除する時刻表を追加
  options = TimetableSetterOptions()
  add_result = await TEST_API.Timetable.set_timetable(
    "To Remove", "Station", "Bound", options
  )
  new_line_id = add_result.unwrap()

  # 存在することを確認
  assert is_successful(await TEST_API.Timetable.get_timetable(new_line_id))

  # 次に、削除
  remove_result = await TEST_API.Timetable.remove_timetable(new_line_id)
  assert is_successful(remove_result)

  # なくなったことを確認
  timetable_result = await TEST_API.Timetable.get_timetable(new_line_id)
  timetable = timetable_result.unwrap()
  assert len(timetable.items) == 0
