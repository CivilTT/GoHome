from returns.pipeline import is_successful

from mock.outerlink import get_links


def test_links():
  """
  リンク集生成モックのテスト

  モック内で有効なデータを２つ生成している
  """
  links = get_links()
  assert is_successful(links)
  assert len(links.unwrap()) == 2

