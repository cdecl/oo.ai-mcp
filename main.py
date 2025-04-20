from playwright.sync_api import sync_playwright
from fastmcp import FastMCP
from markitdown import MarkItDown
import io


mcp = FastMCP("oo.ai-mcp")


def ooai_search(query: str) -> str:
    """Fetches HTML content from oo.ai search results page."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        url = f"https://oo.ai/search?q={query}"
        page.goto(url, wait_until="networkidle")

        content = page.content()
        browser.close()
        return content


def get_page_context(query: str) -> str:
    content = ooai_search(query)
    md = MarkItDown()

    html_stream = io.BytesIO(content.encode('utf-8'))
    result = md.convert_stream(html_stream, format='html')
    return result


@mcp.tool()
def search_content(query: str) -> str:  # Removed async
    """
    Search content on oo.ai using the provided query.
    Args:
        query (str): The search query.
    Returns:
        str: The HTML content of the search results page.
    Example:
        search_ooai_content("example query")
    """
    # Directly call the synchronous search function
    return ooai_search(query)


if __name__ == "__main__":
    mcp.run()
