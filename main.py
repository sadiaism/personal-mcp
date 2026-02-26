from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name= "hello-server",
    stateless_http=True
)

app = mcp.streamable_http_app()