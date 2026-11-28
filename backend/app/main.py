from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.chem import smiles_to_molblock

app = FastAPI(title="OrgoSim")


class MoleculeRequest(BaseModel):
    smiles: str


@app.post("/api/molecule")
def molecule(req: MoleculeRequest):
    molblock = smiles_to_molblock(req.smiles)
    if molblock is None:
        raise HTTPException(status_code=422, detail="Could not build that molecule")
    return {"molblock": molblock}


# Serve the website itself. This must come after the API routes.
FRONTEND = Path(__file__).resolve().parents[2] / "frontend"
app.mount("/", StaticFiles(directory=FRONTEND, html=True), name="frontend")
