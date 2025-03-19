from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


voting_data = {"question": "Čekam unos...", "options": {}, "votes": {}}
connections = []


@app.post("/set_question/")
async def set_question(data: dict):

    voting_data["question"] = data["question"]
    voting_data["options"] = data["options"]
    voting_data["votes"] = {opt: 0 for opt in data["options"]}

    await broadcast()
    return {"message": "Pitanje postavljeno"}


@app.post("/cancel_question/")
async def cancel_question():

    voting_data["question"] = "Trenutno nema pitanja..."
    voting_data["options"] = {}
    voting_data["votes"] = {}

    await broadcast()
    return {"message": "Pitanje obrisano"}


@app.post("/vote/{option}")
async def vote(option: str):

    if option in voting_data["votes"]:
        voting_data["votes"][option] += 1
        await broadcast()
    return {"message": "Glas zabeležen"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """ WebSocket za ažuriranje podataka u realnom vremenu """
    await websocket.accept()
    connections.append(websocket)
    await websocket.send_json(voting_data)

    try:
        while True:
            await asyncio.sleep(1)
            await websocket.send_json(voting_data)
    except:
        connections.remove(websocket)


async def broadcast():
    """ Šalje nove podatke svim povezanim racunarima """
    for connection in connections:
        try:
            await connection.send_json(voting_data)
        except:
            connections.remove(connection)
