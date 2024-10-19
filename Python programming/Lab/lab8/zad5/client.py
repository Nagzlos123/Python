#!/usr/bine/env python3
import asyncio, websockets
#prosty klient
async def client():
    uri = "ws://localhost:8001"
    async with websockets.connect(uri) as websocket:
        message = input("Podaj wiadomosc dla serwera ")
        await websocket.send(message)
        print("Klient wyslal wiadomosc do serwera")
        odpowiedz_ser = await websocket.recv()
        print(f"Wiadomosc od serwer:  {odpowiedz_ser}")
asyncio.get_event_loop().run_until_complete(client())

