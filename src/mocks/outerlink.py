from returns.result import Result, Success

from common.types.outerlink import OuterLink, OuterLinkId

# In-memory store for outer links
__links: list[OuterLink] = [
  OuterLink(id=1, name="Google", url="https://www.google.com"),
  OuterLink(id=2, name="Yahoo", url="https://www.yahoo.co.jp"),
]


def get_links() -> Result[list[OuterLink], Exception]:
  """
  Mock implementation for getting the outer links.
  """
  return Success(__links)


def set_link(name: str, url: str) -> Result[list[OuterLink], Exception]:
  """
  Mock implementation for setting (adding) an outer link.
  """
  new_id = max(link.id for link in __links) + 1 if __links else 1
  new_link = OuterLink(id=new_id, name=name, url=url)
  __links.append(new_link)
  return Success(__links)


def remove_link(link_id: OuterLinkId) -> Result[list[OuterLink], Exception]:
  """
  Mock implementation for removing an outer link.
  """
  global __links
  __links = [link for link in __links if link.id != link_id]
  return Success(__links)
