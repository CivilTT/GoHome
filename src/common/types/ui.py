from pydantic import BaseModel


class ShowingComponents(BaseModel):
  """
  表示するコンポーネント

  @param timetable: 時刻表を表示するかどうか
  @param outerlink: 外部リンクを表示するかどうか
  @param trainInfo: 電車の運行情報を表示するか
  """

  timetable: bool = True
  outerlink: bool = True
  trainInfo: bool = True
