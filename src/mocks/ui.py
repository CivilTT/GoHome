from returns.result import Result, Success

from common.types.ui import ShowingComponents

# 表示コンポーネントのインメモリストア
_showing_components = ShowingComponents(
  timetable=True,
  outerlink=True,
  trainInfo=True,
)


async def get_showing() -> Result[ShowingComponents, Exception]:
  """
  表示コンポーネントを取得するためのモック実装
  """
  return Success(_showing_components.model_copy())


async def set_showing(showing: ShowingComponents) -> Result[None, Exception]:
  """
  表示コンポーネントを設定するためのモック実装
  """
  global _showing_components
  _showing_components = showing
  return Success(None)
