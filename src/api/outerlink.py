from pydantic import BaseModel

from common.types.outerlink import OuterLink, OuterLinkId


# TODO: Result型でラップする
class OuterLinkApi(BaseModel):
  def __init__(self, is_mock_api: bool):
    super().__init__()
    self.is_mock_api = is_mock_api

  @staticmethod
  def get_links() -> list[OuterLink]:
    pass

  @staticmethod
  def set_link(name: str, url: str) -> OuterLinkId:
    pass

  @staticmethod
  def remove_link(link_id: OuterLinkId) -> None:
    pass
