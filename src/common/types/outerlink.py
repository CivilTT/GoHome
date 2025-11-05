from pydantic import AnyUrl, BaseModel

OuterLinkId = int


class OuterLink(BaseModel):
  """
  外部リンク情報

  @param name: リンクの名前
  @param url: リンクのURL
  """

  id: OuterLinkId
  name: str
  url: str | AnyUrl
