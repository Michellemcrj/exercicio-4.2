# Exercício 4.2 — MCP Server para API de Tarefas

MCP server que expõe as tools `criar_tarefa` e `listar_tarefas`, conectando um agente/LLM à API REST do exercício 4.1.

## Arquitetura

```
Agente / LLM  ──MCP──▶  servidor_mcp.py  ──HTTP──▶  API 4.1 (localhost:8000)
```

## Como rodar

A API do exercício 4.1 precisa estar no ar:

```bash
# em exercicio-4.1/
uvicorn app.main:app --reload --port 8000
```

Instalar dependências e testar o MCP server:

```bash
pip install -r requirements.txt
python cliente_teste.py
```

## Tools disponíveis

| Tool | Descrição |
|------|-----------|
| `criar_tarefa(titulo)` | POST /tarefas — cria e devolve o objeto |
| `listar_tarefas()` | GET /tarefas — lista todas as tarefas |
