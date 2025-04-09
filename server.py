from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


@mcp.tool()
def hello_world():
    """
    A simple hello world function.
    """
    return "Hello, world!"

@mcp.tool()
def echo(input: str):
    """
    Echo the input string.
    """
    return f"echo: {input}"

if __name__ == "__main__":
    # Start the server
    mcp.run()
