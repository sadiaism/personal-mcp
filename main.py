from mcp.server.fastmcp import Fastmcp

mcp = FastMCP(
    name= "hello-server",
    stateless_http=True
)

mcp_app = mcp.streamable_http_app()