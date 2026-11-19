<div align="center">

# Práctica #26 — Simulación en Python con Sockets

Servidor web y cliente TCP en Python para demostrar el handshake y el intercambio de datos sobre `localhost`.

[![Licencia](https://img.shields.io/badge/licencia-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Estado](https://img.shields.io/badge/estado-funcional-brightgreen.svg)](#)

</div>

## Sobre el proyecto

Práctica de laboratorio que simula el flujo de una petición HTTP usando sockets crudos. El cliente espera a que el servidor acepte la conexión TCP antes de enviar una petición GET simulada, y el servidor responde con encabezados y HTML estático.

**Objetivo:** comprender el ciclo `socket() → bind() → listen() → accept() → recv() → send()` y su equivalente del lado cliente.

## Características

- Servidor TCP que atiende peticiones en `127.0.0.1:8080`.
- Cliente que construye y envía una petición HTTP/1.1 manual.
- Registro en consola de cada conexión aceptada.
- Manejo de varios clientes con hilos.

## Stack

Python 3.10+ · módulos `socket`, `threading` (sin dependencias externas)

## Instalación

```bash
git clone https://github.com/{{USUARIO}}/practica-26-sockets.git
cd practica-26-sockets
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
```

## Uso

Terminal 1 — servidor:

```bash
python servidor.py
# Escuchando en 127.0.0.1:8080
```

Terminal 2 — cliente:

```bash
python cliente.py
# Conectado. Enviando petición...
```

Salida esperada en el cliente:

```
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

<h1>Hola desde el servidor simulado</h1>
```

Detener el servidor con `Ctrl+C`.

## Estructura

```
practica-26-sockets/
├── servidor.py      # Servidor TCP + respuesta HTTP simulada
├── cliente.py       # Cliente TCP
├── docs/
└── README.md
```

## Alcance

- Solo `localhost`, sin TLS ni DNS.
- Respuestas estáticas; no interpreta rutas ni métodos.
- Uso educativo, no producción.

## Autor

Galan castillo — Práctica #26
