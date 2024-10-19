#!/usr/bin/env python3
import asyncio, websockets 
async def server(websocket, path):
    message = await websocket.recv()
    print(f" Wiadomosc od klienta:  {message}")
    print("Serwer wyslal odpowiedz do klienta")
    greet = "Otrzymalem twoja wiadomosc"
    await websocket.send(greet)
start_server = websockets.serve(server, "localhost", 8001)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


