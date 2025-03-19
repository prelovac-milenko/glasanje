from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI()

# Omogućavanje pristupa sa drugih uređaja
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

voting_data = {"question": "Čekam unos pitanja...", "yes": 0, "no": 0}
connections = []

async def broadcast():
    """Šalje ažurirane podatke svim povezanim klijentima."""
    if connections:
        for conn in connections:
            try:
                await conn.send_json(voting_data)
            except:
                connections.remove(conn)

@app.get("/question")
async def get_question():
    return voting_data

@app.post("/set_question/{question}")
async def set_question(question: str):
    voting_data["question"] = question
    voting_data["yes"] = 0
    voting_data["no"] = 0
    await broadcast()
    return {"message": "Pitanje postavljeno"}

@app.post("/vote/{option}")
async def vote(option: str):
    if option in ["yes", "no"]:
        voting_data[option] += 1
        await broadcast()
        return {"message": "Glas prihvaćen"}
    return {"error": "Nevažeća opcija"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)
    await websocket.send_json(voting_data)  # Odmah šalje trenutno stanje
    try:
        while True:
            await asyncio.sleep(1)  # Drži konekciju otvorenom
            await websocket.send_json(voting_data)
    except:
        connections.remove(websocket)


