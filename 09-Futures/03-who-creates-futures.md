# Who Creates Futures in asyncio?

## ❓ Basic Question
**Who actually creates Future objects in Python? Do we create them manually or does Python handle it?**

---

## 🧠 Simple Answer

👉 Most of the time, **you do NOT create Futures manually**.

They are usually created by:
> the event loop, Tasks, and async libraries (like `asyncio` itself)

---

## ⚙️ Core Idea

Futures are **low-level building blocks** used internally to:

- store results
- notify when something is done
- connect different parts of async system

---

## 🧠 Who Creates Futures?

### 1. 🔄 Event Loop

The event loop creates Futures when:

- handling I/O operations
- managing callbacks
- waiting for external events

👉 It uses Futures to track “when something is ready”

### 2. 🧵 Tasks

When you create a Task:

```python
task = asyncio.create_task(some_coroutine())
```

👉 Internally:
- Task creates a Future
- Stores the result there
- Returns it when awaited

### 3. 📚 Async Libraries

Libraries like:

- networking libraries
- database drivers
- web frameworks

👉 They create Futures to:

- represent ongoing operations
- return results later

### 4. 🧑 (You — Rarely)

You can create Futures manually:

```python
loop.create_future()
```

But:

 - 👉 This is advanced usage
 - 👉 Not needed for beginners

## 🏠 Real-Life Analogy

### 📦 Courier System
- You (user) place request
- Delivery system (event loop) creates tracking record (Future)
- Delivery truck (Task) fulfills request
- When done → tracking shows delivered

👉 You rarely create tracking ID yourself

## ⚠️ Important Insight

👉 Futures are mostly internal glue of asyncio

You usually work with:

 - coroutines (async def)
 - tasks (create_task)
 - await

Not Futures directly

## 🔄 Flow Summary
- Coroutine → wrapped into Task
- Task → uses Future internally
- Future → holds result
- Event loop → manages everything

---

## 🚨 Common Mistake

### ❌ Wrong idea:
> “I need to create Futures to use async”

### ✅ Correct:
> “Futures are handled automatically by asyncio”

---

## 🔥 Key Takeaway

- Futures are created internally by:
  - event loop
  - tasks
  - async libraries
- You rarely need to create them manually
- They are essential but mostly hidden in high-level async code

---

## 🔁 Quick Recap

- Futures store results for later
- Created by event loop and Tasks
- Used internally by asyncio
- Rarely created directly by developers
- Core building block of async system

---

## 🔜 Next Step

👉 Do we use futures directly in real projects?