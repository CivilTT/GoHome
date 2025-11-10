from pydantic import BaseModel
from returns.result import Failure, Result

from api.api import USE_MOCK_API
from common.types.outerlink import OuterLink, OuterLinkId


class OuterLinkApi(BaseModel):
  @staticmethod
  async def get_links() -> Result[list[OuterLink], Exception]:
    """
    UX向上のために画面上に表示するユーザーが設定したリンク集

    TODO: エラーの種類を特定できる場合はExceptionを書き換える
    """
    if USE_MOCK_API:
      from mocks.outerlink import get_links

      return get_links()
    else:
      return Failure(NotImplementedError())

  @staticmethod
  async def set_link(name: str, url: str) -> Result[list[OuterLink], Exception]:
    """
    画面上に表示するリンクを新規設定する

    新規追加した状態の一覧を返す
    """
    if USE_MOCK_API:
      return Failure(NotImplementedError())
    else:
      return Failure(NotImplementedError())

  @staticmethod
  async def remove_link(link_id: OuterLinkId) -> Result[list[OuterLink], Exception]:
    """
    画面上に表示するリンクを削除する

    削除後の一覧を返す
    """
    if USE_MOCK_API:
      return Failure(NotImplementedError())
    else:
      return Failure(NotImplementedError())
