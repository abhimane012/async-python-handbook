# What is an Awaitable?

## ❓ Basic Question
**What does Python mean by “awaitable”? What can actually be used with `await`?**

---

## 🧠 Simple Answer

👉 An *awaitable* is anything that can be used with the `await` keyword.

In simple words:
> “If Python can pause here and resume later, it is awaitable.”

---

## ⚙️ Core Idea

When you write:

```python
result = await something
```

Python expects `something` to be an awaitable object.

📦 Types of Awaitables in Python

There are 3 main kinds:

1. 🔄 Coroutines

Created by `async def`:

```python
async def foo():
    return 10

# Calling it:
coro = foo()   # coroutine object (awaitable)
```

👉 This is the most common awaitable.

2. 🧵 Tasks

Created using `asyncio.create_task()`:

```python
import asyncio

task = asyncio.create_task(foo())
```

👉 A Task is a coroutine that is scheduled to run on the event loop.

3. 🔮 Futures

Lower-level building block used internally by `asyncio`.

- Represents a result that will be available in the future
- Used by the event loop and async libraries

## 🏠 Real-Life Analogy — 📦 “Pending Work Ticket System”

Think of a restaurant:

- Coroutine = order placed 🍔 (not started yet)  
- Task = order sent to kitchen and being processed 👨‍🍳  
- Future = promise that food will arrive later ⏳

👉 All of these are “awaitable” because they represent: “Result will come later”

## ⚡ Key Rule

Only awaitable objects can be used with `await`.

```py
await 10          # ❌ not awaitable
await "hello"     # ❌ not awaitable

await foo()       # ✅ coroutine (awaitable)
await task        # ✅ task (awaitable)
```

## 🧠 Mental Model

| Type       | Is Awaitable? | Meaning                     |
|------------|---------------|-----------------------------|
| Coroutine  | ✅            | Function that can pause     |
| Task       | ✅            | Scheduled coroutine         |
| Future     | ✅            | Placeholder for future result |
| int / str / list | ❌      | Normal values               |

## 🚨 Important Insight

👉 `await` does NOT work on values  
👉 It works only on “future-completion objects”

Because async programming is about: “waiting for something that is not ready yet”

## 🔥 Key Takeaway

An awaitable is anything that:

- can pause execution
- can resume later
- eventually produces a result

## 🔁 Quick Recap

- Awaitable = object that can be used with `await`  
- Main types: coroutine, task, future  
- Normal values are NOT awaitable  
- Awaitables represent “work that completes later”

## 🔜 Next Step

Now that you understand awaitables:

👉 What objects can be awaited?