import pytest
from returns.pipeline import is_successful

from common.types.ui import ShowingComponents
from mocks.ui import get_showing, set_showing


@pytest.mark.asyncio
async def test_get_showing():
  """
  表示コンポーネントの取得をテストします。
  """
  result = await get_showing()
  assert is_successful(result)
  components = result.unwrap()
  assert isinstance(components, ShowingComponents)


@pytest.mark.asyncio
async def test_set_showing():
  """
  表示コンポーネントの設定をテストします。
  """
  # 初期コンポーネントの取得
  initial_components = (await get_showing()).unwrap()

  # 新しいコンポーネントの状態を作成
  new_components_state = ShowingComponents(
    trainInfo=not initial_components.trainInfo,
    timetable=not initial_components.timetable,
    outerlink=not initial_components.outerlink,
  )

  # 新しい状態を設定
  set_result = await set_showing(new_components_state)
  assert is_successful(set_result)

  # 更新された状態を取得
  updated_components_result = await get_showing()
  assert is_successful(updated_components_result)
  updated_components = updated_components_result.unwrap()

  # 状態が更新されたかを確認
  assert updated_components.trainInfo == new_components_state.trainInfo
  assert updated_components.timetable == new_components_state.timetable
  assert updated_components.outerlink == new_components_state.outerlink
