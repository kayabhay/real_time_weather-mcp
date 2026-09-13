from mcp.server.fastmcp import FastMCP 
from tools.weather import get_weather 
from typing import Dict, Any 

mcp = FastMCP("Live Weather")

@mcp.tool()
async def check_weather(location: str) -> str:
    """
    Get real-time weather information for a specified location (e.g. "Paris", "New York", "Tokyo").
    """
    return get_weather(location)


if __name__ == "__main__":
    mcp.run(transport="stdio")