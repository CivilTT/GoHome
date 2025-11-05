from pydantic import BaseModel, ValidationError
from returns.result import Failure, Result, Success


def safe_parse[T: BaseModel](type_obj: type[T], **kwargs) -> Result[T, ValidationError]:
  """
  Pydanticによって実装された型定義によって，内容のバリデーションを安全に行う
  """
  try:
    return Success(type_obj.model_validate(kwargs))
  except ValidationError as e:
    return Failure(e)
