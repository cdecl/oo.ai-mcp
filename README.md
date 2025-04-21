# oo

This project provides a tool to search content on oo.ai.

## Usage

```python
from oo.main import search_ooai

# Search content on oo.ai
result = search_ooai("example query")
print(result)
```

## Dependencies

- fastmcp>=2.2.0
- markitdown[all]>=0.1.1
- playwright>=1.51.0
- pytest>=8.3.5

## Requirements

- Python 3.13 or higher

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/cdecl/oo.ai-mcp
   cd oo
   ```

2. Install the package:

   ```bash
   uv pip install .
   ```

3. Sync the dependencies:

   ```bash
   uv sync
   ```

## Running the server

```bash
uv run oo
```

## MCP Server Registration

To use this tool as an MCP server, register it in your MCP configuration with the following details:

```json
{
  "name": "oo.ai-mcp",
  "command": "uv run --directory /Users/cdecl/Downloads/oo src/main.py"
}
```

## Testing

```bash
pytest
```
