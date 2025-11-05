from pydantic import BaseModel
from returns.result import Failure, Result

from api.api import USE_MOCK_API
from common.types.outerlink import OuterLink, OuterLinkId


class OuterLinkApi(BaseModel):
  @staticmethod
  def get_links() -> Result[list[OuterLink], Exception]:
    """
    UX向上のために画面上に表示するユーザーが設定したリンク集

    TODO: エラーの種類を特定できる場合はExceptionを書き換える
    """
    if USE_MOCK_API:
      from mock.outerlink import get_links

      return get_links()
    else:
      return Failure(NotImplementedError())

  @staticmethod
  def set_link(name: str, url: str) -> Result[OuterLinkId, Exception]:
    """
    画面上に表示するリンクを新規設定する
    """
    if USE_MOCK_API:
      return Failure(NotImplementedError())
    else:
      return Failure(NotImplementedError())

  @staticmethod
  def remove_link(link_id: OuterLinkId) -> Result[None, Exception]:
    """
    画面上に表示するリンクを削除する
    """
    if USE_MOCK_API:
      return Failure(NotImplementedError())
    else:
      return Failure(NotImplementedError())
