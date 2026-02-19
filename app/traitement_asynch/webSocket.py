from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import asyncio

router = APIRouter()

@router.websocket("/ws/hello")
async def websocket_hello(websocket: WebSocket):
    await websocket.accept()
    print("Client connecté")
    try:
        while True:
            print("activation de websocket")  # ⚡ juste afficher "bonjour"
            await asyncio.sleep(10)  # ⚡ pause 10 secondes
    except WebSocketDisconnect:
        print("Client déconnecté")
    except asyncio.CancelledError:
        print("WebSocket annulé (serveur arrêté ou tâche interrompue)")
    except Exception as e:
        print("Erreur WebSocket inattendue :", e)
