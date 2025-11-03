from pydantic import BaseModel
from returns.result import Result

from common.types.outerlink import OuterLink, OuterLinkId


class OuterLinkApi(BaseModel):
  def __init__(self, is_mock_api: bool):
    super().__init__()
    self.is_mock_api = is_mock_api

  @staticmethod
  def get_links() -> Result[list[OuterLink]]:
    pass

  @staticmethod
  def set_link(name: str, url: str) -> Result[OuterLinkId]:
    pass

  @staticmethod
  def remove_link(link_id: OuterLinkId) -> Result[None]:
    pass
