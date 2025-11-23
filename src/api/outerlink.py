from returns.result import Failure, Result

from common.types.api import BaseApi
from common.types.outerlink import OuterLink, OuterLinkId


class OuterLinkApi(BaseApi):
  async def get_links(self) -> Result[list[OuterLink], Exception]:
    """
    UX向上のために画面上に表示するユーザーが設定したリンク集

    TODO: エラーの種類を特定できる場合はExceptionを書き換える
    """
    if self.use_mock_api:
      from mocks.outerlink import get_links

      return await get_links()
    else:
      return Failure(NotImplementedError())

  async def set_link(self, name: str, url: str) -> Result[list[OuterLink], Exception]:
    """
    画面上に表示するリンクを新規設定する

    新規追加した状態の一覧を返す
    """
    if self.use_mock_api:
      from mocks.outerlink import set_link

      return await set_link(name, url)
    else:
      return Failure(NotImplementedError())

  async def remove_link(
    self, link_id: OuterLinkId
  ) -> Result[list[OuterLink], Exception]:
    """
    画面上に表示するリンクを削除する

    削除後の一覧を返す
    """
    if self.use_mock_api:
      from mocks.outerlink import remove_link

      return await remove_link(link_id)
    else:
      return Failure(NotImplementedError())
