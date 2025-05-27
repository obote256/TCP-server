# Simple Python TCP Server

A basic TCP server implemented in Python that runs on localhost. It handles multiple client connections concurrently using threading, making it suitable for simple network communication tasks and learning purposes.

## Features

- Listens for TCP connections on localhost.
- Supports multiple clients simultaneously using threading.
- Easy to understand and extend.

## Requirements

- Python 3.x
- `socket` module (comes pre-installed with Python standard library)
- `threading` module (comes pre-installed with Python standard library)

> **Note:** Both `socket` and `threading` are included with the Python standard library, so no additional installation is required.

## How to Use

1. Make sure Python 3 is installed on your system.
2. Run the TCP server script:
   ```bash
   python tcp_server.py
