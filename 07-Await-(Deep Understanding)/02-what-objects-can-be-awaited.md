# What Objects Can Be Awaited?

## ❓ Basic Question
**In Python, what exactly can we use with the `await` keyword?**

---

## 🧠 Simple Answer

👉 You can `await` only objects that are **awaitable**.

An object is awaitable if Python treats it as:

> “This will produce a result in the future, so I can pause here and resume later.”

---

## 📦 Main Types of Awaitable Objects

There are **3 main categories** you can await in Python:

### 1. 🔄 Coroutines
Created using `async def`

```python
async def fetch_data():
    return 42
```

Calling it:

```python
coro = fetch_data()  # coroutine object
result = await fetch_data()  # await returns 42 when coroutine runs
```

### 2. 🧵 Tasks
Created using `asyncio.create_task()`:

```python
import asyncio

task = asyncio.create_task(fetch_data())
result = await task
```

💡 A Task = a coroutine that has been scheduled on the event loop.

### 3. 🔮 Futures
Low-level async objects used internally by `asyncio`. Represent a result that will be available later.

```python
loop = asyncio.get_event_loop()
future = loop.create_future()
result = await future
```

---

## 🏠 Real-Life Analogy

### 📦 Waiting List System  
Coroutine = you placed an order 🍔  
Task = order is already in the kitchen queue 👨‍🍳  
Future = promise that the order will arrive later ⏳

👉 All are valid because they represent: “result not ready yet, but will come later”

---

## 🚫 What You CANNOT Await

Normal values cannot be awaited:

```python
await 10          # ❌ TypeError
await "hello"     # ❌ TypeError
await [1, 2, 3]   # ❌ TypeError
```

👉 Because these are already “ready values”, not future results.

---

## ⚙️ Internal Rule

Python checks: does this object implement `__await__()`?

- If yes → it is awaitable  
- If no  → `TypeError: object is not awaitable`

---

## 🧠 Mental Model

| Object Type | Awaitable? | Why |
|-------------|------------|-----|
| Coroutine   | ✅         | Can pause/resume |
| Task        | ✅         | Scheduled coroutine |
| Future      | ✅         | Pending result |
| int / str / list | ❌   | Already completed value |

---

## 🔥 Key Insight

👉 `await` is NOT for “doing work” — it is for “waiting for future work to finish”.

---

## ⚠️ Common Mistake

❌ Wrong thinking: “I can await anything slow”  
✅ Correct thinking: “I can only await objects designed for async execution”

---

## 🔁 Quick Recap

- Only awaitable objects can be used with `await`  
- Main awaitables: coroutine, task, future  
- Normal values cannot be awaited  
- Awaitables represent “future results”

---

## 🔜 Next Step

Now that you understand what can be awaited:

👉 Does await block the program?