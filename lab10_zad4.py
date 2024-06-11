import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(f"Odebrano: {message}")
        await websocket.send(message)
        print(f"Wysłano: {message}")

start_server = websockets.serve(echo, "127.0.0.1", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
print("Serwer WebSocket działa na porcie 8765")
asyncio.get_event_loop().run_forever()
