from mcp.server.fastmcp import FastMCP
from tools.weather import get_weather

mcp = FastMCP("Live Weather")


@mcp.tool()
async def check_weather(location: str, detailed: bool = False) -> str:
    """
    Get real-time weather information for a specified location (e.g., "Paris", "New York", "Tokyo").

    Args:
        location: City or location name.
        detailed: If True, includes feels-like temperature, humidity, wind, and precipitation.
    """
    return get_weather(location, detailed=detailed)


if __name__ == "__main__":
    mcp.run(transport="stdio")