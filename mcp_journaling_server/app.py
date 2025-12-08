"""
FastMCP quickstart example.

Run from the repository root:
    uv run examples/snippets/servers/fastmcp_quickstart.py
"""

from utils import write_content, get_content
from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession
from mcp.types import SamplingMessage, TextContent

# Create an MCP server
mcp = FastMCP("Journaling App", json_response=True)


# Add an addition tool
@mcp.tool()
def add_note_to_journal(data: str, date=None) -> str:
    """Make a journal for the given date (YYYY-MM-DD)"""
    if write_content(data, date):
        return "Your memories from this day has been saved! Happy Journaling!"
    else:
        return "Try again :("
    
@mcp.tool()
def read_journal(start_date=None, end_date=None):
    """Read journal from given start_date (YYYY-MM-DD) to end_date (YYYY-MM-DD)"""
    content = get_content(start_date, end_date)
    if content:
        return content
    else:
        return "There are no journals yet :("
    
@mcp.tool()
def read_journal(start_date=None, end_date=None):
    """Read journal from given start_date (YYYY-MM-DD) to end_date (YYYY-MM-DD)"""
    content = get_content(start_date, end_date)
    if content:
        return content
    else:
        return "There are no journals yet :("


@mcp.tool()
async def summarise_journal(start_date=None, end_date=None) -> str:
    """Summarise journal enteries. Mention highlights, ideas, happy moments, action items."""
    prompt = """Summarize the following journal entry clearly and concisely.
                Organize the summary into these sections-
                People I interacted with - 
                Highlights – Key events, wins, meaningful moments.
                Happy Moments – Anything that brought joy, positivity, or gratitude.
                Sad Moments - Anything that brought sadness, aggression, or disappointment.
                Struggles – Challenges, obstacles, confusions.
                Ideas – New thoughts, insights, plans, creative sparks.
                Action Items – Tasks, next steps, things to follow up on.
                One word - summarise in one word.
                Output format-
                Keep it short simple and sweet
                Use short bullet points under each section.
                Keep wording simple and clear.
                Preserve important context but remove unnecessary details.
                Journal Entry-""" + get_content()
    
    return prompt
    

# Run with streamable HTTP transport
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
