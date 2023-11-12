import asyncio
import websockets

async def server(websocket, path):
    # Register the websocket
    clients.add(websocket)
    try:
        async for message in websocket:
            # Broadcast the message to all other clients
            for client in clients:
                if client != websocket and client.open:
                    await client.send(message)
    finally:
        # Unregister the websocket when the connection is closed
        clients.remove(websocket)

# Set up the WebSocket server
clients = set()
start_server = websockets.serve(server, "127.0.0.1", 3000)

print("Server is running...")

# Start the event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

