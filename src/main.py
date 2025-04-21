from playwright.async_api import async_playwright  # Changed to async_api
from fastmcp import FastMCP
from markitdown import MarkItDown
import io
import asyncio
# Removed unused asyncio import

mcp = FastMCP("oo.ai-mcp")


async def ooai_search(query: str) -> str:  # Changed to async def
    """Fetches HTML content from oo.ai search results page."""
    async with async_playwright() as p:  # Changed to async_playwright
        browser = await p.chromium.launch(headless=True)  # Added await
        page = await browser.new_page()  # Added await

        url = f"https://oo.ai/search?q={query}"
        await page.goto(url, wait_until="networkidle")  # Added await

        content = await page.content()  # Added await
        await browser.close()  # Added await
        return content


async def get_page_context(query: str) -> str:  # Changed to async def
    content = await ooai_search(query)  # Added await
    md = MarkItDown()

    html_stream = io.BytesIO(content.encode('utf-8'))
    # MarkItDown might not be async, assuming convert_stream is sync
    result = md.convert_stream(html_stream, format='html')
    return result


@mcp.tool()
async def search_ooai(query: str) -> str:  # Changed to async def
    """
    Search content on oo.ai using the provided query.
    Args:
        query (str): The search query.
    Returns:
        str: The HTML content of the search results page.
    Example:
        search_ooai("example query")
    """
    # Call the asynchronous search function
    return await get_page_context(query)  # Added await


def main():
    asyncio.run(mcp.run())  # Added asyncio.run


if __name__ == "__main__":
    main()
