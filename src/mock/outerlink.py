from random import random

from returns.pipeline import is_successful
from returns.result import Failure, Success

from common.scripts.types.parser import safe_parse
from common.types.outerlink import OuterLink


def get_links():
  samples = [
    {"name": "Google", "url": "https://www.google.com"},
    {"name": "Yahoo", "url": "https://www.yahoo.co.jp"},
    {"name": 3, "url": "not a url"},
  ]
  sampleIds = [int(random()) for _ in range(len(samples))]

  parsed = [
    safe_parse(OuterLink, id=link_id, **data)
    for link_id, data in zip(sampleIds, samples, strict=True)
  ]
  filtered = list(filter(is_successful, parsed))
  cleaned = [x.unwrap() for x in filtered]

  if len(filtered) > 0:
    return Success(cleaned)
  else:
    return Failure(ValueError("All data are invalid schema."))
