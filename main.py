from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Cho phép ChatGPT truy cập (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/manifest.json")
async def manifest():
    data = {
        "name": "ghidra_mcp",
        "version": "1.0.0",
        "description": "Bridge between ChatGPT and Ghidra reverse engineering instance",
        "author": "G14 (Tiến Khải Nguyễn)",
        "license": "MIT",
        "endpoints": {
            "sse": "https://ghidra-mcp.onrender.com/sse"
        },
        "capabilities": {"tools": True},
        "tools": [
            {
                "name": "decompile_function",
                "description": "Decompile a function from the Ghidra project",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "function_name": {
                            "type": "string",
                            "description": "Name of the function to decompile"
                        }
                    },
                    "required": ["function_name"]
                }
            },
            {
                "name": "list_functions",
                "description": "List all functions in the current Ghidra project",
                "input_schema": {
                    "type": "object",
                    "properties": {}
                }
            }
        ]
    }
    return JSONResponse(content=data, headers={"Cache-Control": "no-cache"})

@app.get("/")
async def root():
    return {"message": "✅ Ghidra MCP FastAPI server is running!"}
