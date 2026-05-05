# Which Libraries Support Async I/O in Python?

## ❓ Basic Question
**Which Python libraries can we use to write async (non-blocking) I/O code?**

---

## 🧠 Simple Answer

👉 Python provides built-in and third-party libraries that support async I/O.

They help you:
- make non-blocking network calls
- handle many requests efficiently
- build scalable systems

---

## ⚙️ Categories of Async Libraries

### 1. 🧱 Built-in Library

### 🔹 asyncio

👉 Core async framework in Python

- event loop
- tasks
- coroutines
- async utilities

💡 Everything in async Python is built on top of this


### 2. 🌐 HTTP / Network Libraries

### 🔹 aiohttp

👉 Async HTTP client & server

Use for:
- API calls
- web servers

---

### 🔹 httpx (async mode)

👉 Modern HTTP client (supports both sync & async)

Use for:
- REST APIs
- external service calls


### 3. 🗄️ Database Libraries


### 🔹 asyncpg

👉 Async PostgreSQL driver

---

### 🔹 databases

👉 Async DB layer (works with multiple databases)

---

### 🔹 aiomysql

👉 Async MySQL client


### 4. 📁 File I/O Libraries

---

### 🔹 aiofiles

👉 Async file read/write operations

---

### 5. 🚀 Web Frameworks

### 🔹 FastAPI

👉 Modern async web framework

- built on asyncio
- very high performance

---

### 🔹 Sanic

👉 Async web server framework

---

### 🔹 Starlette

👉 Lightweight async framework (used by FastAPI)


### 6. 🔄 Utility Libraries

### 🔹 anyio

👉 Abstraction layer over asyncio & others

---

### 🔹 trio

👉 Alternative async framework (different model)

---

## 🏠 Real-Life Analogy

### 🏗️ Building a Web App

- asyncio → foundation 🧱  
- aiohttp/httpx → communication 🌐  
- asyncpg → database 🗄️  
- FastAPI → full application 🚀  

👉 All work together to build async systems

---

## ⚠️ Important Insight

👉 Not all Python libraries are async

- Some are blocking (e.g., `requests`)
- Some support async (e.g., `httpx`, `aiohttp`)

👉 Using blocking libraries inside async code breaks concurrency

---

## 🚨 Common Mistake

### ❌ Wrong:
> Using blocking libraries inside async functions

Example:
- using `requests` inside `async def`

👉 This blocks the event loop

---

### ✅ Correct:
> Use async-compatible libraries


## 🧠 Mental Model

```
asyncio → engine libraries → tools built on engine
```


## 🔥 Key Takeaway

- asyncio is the core async system
- multiple libraries extend async capabilities
- use async-compatible tools for best performance
- essential for modern scalable Python apps

---

## 🔁 Quick Recap

- asyncio = built-in async framework
- aiohttp / httpx = network calls
- asyncpg / aiomysql = databases
- aiofiles = file I/O
- FastAPI / Starlette = web frameworks
- trio / anyio = alternative async systems

---   

## 🔜 Next Step

👉 What are common mistakes developers make when using async libraries?