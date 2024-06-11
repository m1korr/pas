import asyncio
import websockets

async def hello():
    uri = "wss://echo.websocket.org"
    #uri = "ws://127.0.0.1:8765"
    async with websockets.connect(uri) as websocket:
        print(f"Połączono z {uri}")

asyncio.get_event_loop().run_until_complete(hello())
