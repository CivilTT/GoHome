import pytest
from returns.pipeline import is_successful

from api.api import Api

TEST_API = Api(True)


@pytest.mark.asyncio
async def test_get_links():
  """
  リンクのリスト取得をテストします。
  """
  links_result = await TEST_API.OuterLink.get_links()
  assert is_successful(links_result)
  links = links_result.unwrap()
  assert isinstance(links, list)
  # モックは2つのリンクで初期化されます
  assert len(links) == 2


@pytest.mark.asyncio
async def test_set_link():
  """
  新しいリンクの追加をテストします。
  """
  initial_links = await TEST_API.OuterLink.get_links()
  initial_links_count = len(initial_links.unwrap())

  # 新しいリンクを追加
  set_result = await TEST_API.OuterLink.set_link("New Link", "https://example.com")
  assert is_successful(set_result)
  updated_links = set_result.unwrap()

  # リンクが追加されたことを確認
  assert len(updated_links) == initial_links_count + 1
  assert updated_links[-1].name == "New Link"


@pytest.mark.asyncio
async def test_remove_link():
  """
  リンクの削除をテストします。
  """
  # 削除するIDを持つために初期リンクを取得

  initial_links = (await TEST_API.OuterLink.get_links()).unwrap()
  if not initial_links:
    # 削除するものが何もない場合に備えてリンクを追加
    await TEST_API.OuterLink.set_link("Test", "https://test.com")
    initial_links = (await TEST_API.OuterLink.get_links()).unwrap()

  link_to_remove = initial_links[0]
  initial_links_count = len(initial_links)

  # リンクを削除
  remove_result = await TEST_API.OuterLink.remove_link(link_to_remove.id)
  assert is_successful(remove_result)
  updated_links = remove_result.unwrap()

  # リンクが削除されたことを確認
  assert len(updated_links) == initial_links_count - 1
  assert all(link.id != link_to_remove.id for link in updated_links)
