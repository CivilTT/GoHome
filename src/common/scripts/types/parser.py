from typing import Any

from pydantic import BaseModel, ValidationError
from returns.result import Failure, Result, Success


def safe_parse[T: BaseModel](
  type_obj: type[T], **kwargs: Any
) -> Result[T, ValidationError]:
  """
  Pydanticによって実装された型定義によって，内容のバリデーションを安全に行う
  """
  try:
    parsed:T = type_obj.model_validate(kwargs)
    return Success(parsed)
  except ValidationError as e:
    return Failure(e)
