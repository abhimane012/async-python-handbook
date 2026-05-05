# How Do We Handle Exceptions in Async Code?

## ❓ Basic Question
**How do errors work in async Python, and how do we properly handle them?**

---

## 🧠 Simple Answer

👉 Exception handling in async code works the same as normal Python:
> You use `try` / `except`

BUT there is an extra layer:
- exceptions inside **Tasks** behave differently than direct `await`

---

## ⚙️ Core Idea

There are 3 common async scenarios:

1. `await coroutine()`
2. `asyncio.create_task()`
3. `asyncio.gather()`

Each handles exceptions slightly differently.

---

### 1. 🟢 Exceptions with `await`

```python
result = await some_async_function()
```
What happens:
- If error occurs → it is raised immediately
    - You can catch it normally
- Handling:
    - use try/except around await

👉 This is the simplest case

### 2. 🧵 Exceptions in create_task()
```python
task = asyncio.create_task(some_async_function())
```
- What happens:
    - Task runs in background
    - Exception does NOT appear immediately
    - It is stored inside the Task

- Problem:
    - If you never await or inspect it:
    - exception may be silently ignored or logged as warning
Proper handling:

        - You must do one of these:
            - ```await task or task.exception()```

### 3. ⚡ Exceptions in asyncio.gather()
- await asyncio.gather(a(), b(), c())
- Default behavior:
    - if ANY task fails → gather raises exception immediately
- Handling option:
    - You can control behavior using:
    - return_exceptions=True
- Then:
    - errors are returned as values instead of crashing

## 🏠 Real-Life Analogy

### 📦 Delivery System
- await → you are directly waiting for one delivery 🚚
- create_task → delivery is happening in background 📦
- gather → multiple deliveries tracked together 📦📦📦

👉 If something fails:

- direct wait → you see it immediately
- background task → you must check later
- gather → system reports it collectively

## 🧠 Mental Model
- await → immediate error
- task → hidden until checked
- gather → grouped error handling

## ⚠️ Common Mistakes

### ❌ Ignoring Task exceptions
- creating tasks and never awaiting them leads to silent failures

### ❌ Not handling gather failures
- one failure stops all results

## 🔥 Best Practices

### 1. Always handle await errors
```python
try:
    await func()
except Exception:
    ...
```

### 2. Always track tasks
- store task reference
- await or inspect later

### 3. Use gather carefully
- use return_exceptions=True when partial failure is acceptable

## 📊 Summary Table
| Method        | Exception Behavior          |
|---------------|----------------------------|
| await         | Immediate raise            |
| create_task() | Stored inside task         |
| gather()      | Raises or returns list     |

## 🔁 Quick Recap
- Async exceptions work like normal Python

    - await → immediate handling
    - Task → deferred handling
    - gather → collective handling
    - Always ensure tasks are awaited or monitored

## 🔜 Next Step

👉 What happens if one task fails?