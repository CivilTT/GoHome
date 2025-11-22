import pytest
from returns.pipeline import is_successful

from api.api import Api
from common.types.ui import ShowingComponents

TEST_API = Api(True)


@pytest.mark.asyncio
async def test_get_showing():
  """
  表示コンポーネントの取得をテストします。
  """
  result = await TEST_API.Ui.get_showing()
  assert is_successful(result)
  components = result.unwrap()
  assert isinstance(components, ShowingComponents)


@pytest.mark.asyncio
async def test_set_showing():
  """
  表示コンポーネントの設定をテストします。
  """
  # 初期コンポーネントの取得
  initial_components = (await TEST_API.Ui.get_showing()).unwrap()

  # 新しいコンポーネントの状態を作成
  new_components_state = ShowingComponents(
    trainInfo=not initial_components.trainInfo,
    timetable=not initial_components.timetable,
    outerlink=not initial_components.outerlink,
  )

  # 新しい状態を設定
  set_result = await TEST_API.Ui.set_showing(new_components_state)
  assert is_successful(set_result)

  # 更新された状態を取得
  updated_components_result = await TEST_API.Ui.get_showing()
  assert is_successful(updated_components_result)
  updated_components = updated_components_result.unwrap()

  # 状態が更新されたかを確認
  assert updated_components.trainInfo == new_components_state.trainInfo
  assert updated_components.timetable == new_components_state.timetable
  assert updated_components.outerlink == new_components_state.outerlink
