# 🌤️ Real-Time Weather MCP Server

A Model Context Protocol (MCP) server that provides real-time weather information to Claude Desktop and any other MCP-compliant client. Built using [FastMCP](https://github.com/modelcontextprotocol/python-sdk).

---

## ✨ Features

- **Live Weather Data**: Real-time conditions, temperatures, and forecasts.
- **Zero API Key Requirement**: Uses `wttr.in` without requiring sign-up or paid subscription keys.
- **FastMCP Powered**: High-performance asynchronous tool handling over standard input/output (`stdio`).
- **Claude Desktop Ready**: One-click registration using the `mcp` CLI or manual JSON configuration.

---

## 📁 Project Structure

```text
real_time_weather-mcp/
├── main.py              # FastMCP server entry point & tool registration
├── tools/
│   ├── __init__.py      # Tools package initializer
│   └── weather.py       # Weather fetching logic & API handler
├── pyproject.toml       # Modern Python packaging & dependencies
├── requirements.txt     # Standard pip requirements file
├── .gitignore           # Git ignore configuration
├── LICENSE              # MIT License
└── README.md            # Project documentation
```

---

## 🛠️ Prerequisites

- **Python**: `>= 3.10`
- **uv** (recommended) or standard `pip`
- **Claude Desktop** (optional, for LLM integration)

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/real_time_weather-mcp.git
cd real_time_weather-mcp
```

### 2. Set up environment & install dependencies

**Using `uv` (recommended):**
```bash
uv venv
.venv\Scripts\activate   # On Windows (or 'source .venv/bin/activate' on macOS/Linux)
uv pip install -e .
```

**Using standard `pip`:**
```bash
python -m venv .venv
.venv\Scripts\activate   # On Windows (or 'source .venv/bin/activate' on macOS/Linux)
pip install -r requirements.txt
```

---

## 🔌 Installing into Claude Desktop

### Automatic Installation

Run the FastMCP installer from your activated virtual environment:

```bash
mcp install main.py
```

> **Note for Windows Store Claude users:** If your Claude app was installed from the Microsoft Store, ensure `AppData\Roaming\Claude` points or links to your local package cache.

### Manual Configuration

Add the following to your `claude_desktop_config.json`:

- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "Live Weather": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "/absolute/path/to/real_time_weather-mcp/main.py"
      ]
    }
  }
}
```

Restart Claude Desktop to activate the tool.

---

## 🧪 Testing & Debugging

You can test the MCP server using the official MCP Inspector:

```bash
npx @modelcontextprotocol/inspector uv run main.py
```

Or run the server directly in stdio mode:

```bash
python main.py
```

---

## 🛠️ Available MCP Tools

| Tool | Parameters | Description |
| :--- | :--- | :--- |
| `check_weather` | `location` (*string*) | Fetches real-time weather information for the specified city or region (e.g., `"Paris"`, `"New York"`, `"Tokyo"`). |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
