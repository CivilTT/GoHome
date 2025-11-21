from returns.result import Result, Success

from common.types.ui import ShowingComponents

# 表示コンポーネントのインメモリストア
__showing_components = ShowingComponents(
  timetable=True,
  outerlink=True,
  trainInfo=True,
)


def get_showing() -> Result[ShowingComponents, Exception]:
  """
  表示コンポーネントを取得するためのモック実装
  """
  return Success(__showing_components)


def set_showing(showing: ShowingComponents) -> Result[None, Exception]:
  """
  表示コンポーネントを設定するためのモック実装
  """
  global __showing_components
  __showing_components = showing
  return Success(None)
