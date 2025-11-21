from returns.pipeline import is_successful

from mocks.outerlink import get_links, remove_link, set_link


def test_get_links():
    """
    Test getting the list of links.
    """
    links_result = get_links()
    assert is_successful(links_result)
    links = links_result.unwrap()
    assert isinstance(links, list)
    # The mock is initialized with 2 links
    assert len(links) == 2


def test_set_link():
    """
    Test adding a new link.
    """
    initial_links_count = len(get_links().unwrap())

    # Add a new link
    set_result = set_link("New Link", "https://example.com")
    assert is_successful(set_result)
    updated_links = set_result.unwrap()

    # Check that the link was added
    assert len(updated_links) == initial_links_count + 1
    assert updated_links[-1].name == "New Link"


def test_remove_link():
    """
    Test removing a link.
    """
    # Get initial links to have an ID to remove
    initial_links = get_links().unwrap()
    if not initial_links:
        # Add a link to ensure there is something to remove
        set_link("Test", "https://test.com")
        initial_links = get_links().unwrap()

    link_to_remove = initial_links[0]
    initial_links_count = len(initial_links)

    # Remove the link
    remove_result = remove_link(link_to_remove.id)
    assert is_successful(remove_result)
    updated_links = remove_result.unwrap()

    # Check that the link was removed
    assert len(updated_links) == initial_links_count - 1
    assert all(link.id != link_to_remove.id for link in updated_links)