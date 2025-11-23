from returns.result import Result, Success

from common.types.outerlink import OuterLink, OuterLinkId

# 外部リンクのインメモリストア
_links: list[OuterLink] = [
  OuterLink(id=1, name="Google", url="https://www.google.com"),
  OuterLink(id=2, name="Yahoo", url="https://www.yahoo.co.jp"),
]


async def get_links() -> Result[list[OuterLink], Exception]:
  """
  外部リンクを取得するためのモック実装
  """
  return Success(_links.copy())


async def set_link(name: str, url: str) -> Result[list[OuterLink], Exception]:
  """
  外部リンクを設定（追加）するためのモック実装
  """
  new_id = max(link.id for link in _links) + 1 if _links else 1
  new_link = OuterLink(id=new_id, name=name, url=url)
  _links.append(new_link)
  return Success(_links.copy())


async def remove_link(link_id: OuterLinkId) -> Result[list[OuterLink], Exception]:
  """
  外部リンクを削除するためのモック実装
  """
  global _links
  _links = [link for link in _links if link.id != link_id]
  return Success(_links.copy())
