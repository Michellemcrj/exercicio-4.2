from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Store em memória. Zera quando o processo reinicia.
_tarefas: dict[int, dict] = {}
_proximo_id = 1


class TarefaIn(BaseModel):
    titulo: str


class TarefaUpdate(BaseModel):
    titulo: str
    concluida: bool


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tarefas", status_code=201)
def criar(tarefa: TarefaIn):
    global _proximo_id
    nova = {"id": _proximo_id, "titulo": tarefa.titulo, "concluida": False}
    _tarefas[_proximo_id] = nova
    _proximo_id += 1
    return nova


@app.get("/tarefas")
def listar():
    return list(_tarefas.values())


@app.get("/tarefas/{id}")
def buscar(id: int):
    if id not in _tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return _tarefas[id]


@app.put("/tarefas/{id}")
def atualizar(id: int, dados: TarefaUpdate):
    if id not in _tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    _tarefas[id] = {"id": id, "titulo": dados.titulo, "concluida": dados.concluida}
    return _tarefas[id]
