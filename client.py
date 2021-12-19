import asyncio
import websockets

HOST = 'localhost'
PORT = 8000


async def hello():
    async with websockets.connect("ws://localhost:8000/ws") as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()


asyncio.run(hello())
