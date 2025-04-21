
import pytest
import asyncio

from main import get_page_context


def test_get_page_context():
    query = "파이선 프로그래밍"
    print("Query:", query)

    content = asyncio.run(get_page_context(query))  # Using asyncio.run to run the async function
    # content = await get_page_context(query)
    print(content)

    assert content != ""

