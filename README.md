# Python Socket Examples

This repository demonstrates simple socket programming examples in Python.

## Steps

1. **Step 1** - Basic TCP client and server.
2. **Step 2** - TCP server handling multiple clients.
3. **Step 3** - TCP server sends replies to clients.
4. **Step 4** - UDP server and clients.

Each step has its own server and client scripts:

- `step1_server.py` / `step1_client.py`
- `step2_server.py` / `step2_client.py`
- `step3_server.py` / `step3_client.py`
- `step4_server.py` / `step4_client.py`

## Running the examples

Open two terminals for TCP steps. Start the server first, then run the client (or clients). For example:

```bash
python step1_server.py  # Terminal 1
python step1_client.py  # Terminal 2
```

For the multi-client steps (`step2_client.py`, `step3_client.py`, `step4_client.py`), the script automatically spawns 10 client connections.
