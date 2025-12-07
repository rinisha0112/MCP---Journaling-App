"""
FastMCP quickstart example.

Run from the repository root:
    uv run examples/snippets/servers/fastmcp_quickstart.py
"""

from mcp.server.fastmcp import FastMCP
from utils import write_content, get_content

# Create an MCP server
mcp = FastMCP("Journaling App", json_response=True)


# Add an addition tool
@mcp.tool()
def add_note_to_journal(data: str) -> str:
    """Make a journal for today"""
    if write_content(data):
        return "Your memories from this day has been saved! Happy Journaling!"
    else:
        return "Try again :("
    
@mcp.tool()
def read_journal():
    content = get_content()
    if content:
        return content
    else:
        return "There are no journals yet :("
    

# Run with streamable HTTP transport
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
