import urllib.error
import urllib.parse
import urllib.request

__all__ = ["get_weather"]


def get_weather(location: str, detailed: bool = False) -> str:
    """
    Fetches the weather for a given location using wttr.in.

    Args:
        location (str): The city or location name (e.g., "New York", "London", "Tokyo").
        detailed (bool): If True, returns detailed metrics including feels-like temperature,
                         humidity, wind, and precipitation. Defaults to False.

    Returns:
        str: Weather information for the location, or a helpful error message.
    """
    clean_location = location.strip() if location else ""
    if not clean_location:
        return "Error: Location cannot be empty. Please provide a city or place name."

    try:
        encoded_location = urllib.parse.quote(clean_location)
        if detailed:
            fmt = urllib.parse.quote("%l: %c %t (Feels like %f) | Wind: %w | Humidity: %h | Precip: %p")
        else:
            fmt = "3"

        url = f"https://wttr.in/{encoded_location}?format={fmt}"
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "curl/7.68.0"}
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            result = response.read().decode("utf-8").strip()
            if not result or "Unknown location" in result:
                return f"Could not find weather data for '{clean_location}'. Please verify the location name."
            return result

    except urllib.error.HTTPError as e:
        if e.code in (404, 500):
            return f"Could not find weather data for '{clean_location}'. Please check the spelling and try again."
        return f"Weather service error (HTTP {e.code}) while fetching data for '{clean_location}'."
    except urllib.error.URLError as e:
        return f"Network error connecting to weather service: {e.reason}"
    except TimeoutError:
        return f"Request timed out while fetching weather for '{clean_location}'."
    except Exception as e:
        return f"Unexpected error while fetching weather: {e}"


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    print("Concise:", get_weather("Pune"))
    print("Detailed:", get_weather("Pune", detailed=True))
