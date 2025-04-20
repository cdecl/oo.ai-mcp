
import pytest

from main import get_page_context


def test_get_page_context():
    query = "파이선 프로그래밍"
    print("Query:", query)

    content = get_page_context(query)
    print(content)

    assert content != ""

