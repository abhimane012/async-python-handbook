# What Does the `async` Keyword Do?

## ❓ Basic question
**What happens when we write `async def` in Python? Why do we need the `async` keyword?**

---

## 🧠 Simple answer
The `async` keyword turns a normal function into a *coroutine function*. It tells Python: “This function can pause, resume, and work with the event loop.”

---

## ⚙️ What `async` actually changes

```python
async def my_function():
    ...
```

When you write the above:

- It becomes a *coroutine function*.
- Calling it returns a *coroutine object* (it is not executed immediately).
- It can use `await` inside.
- It must be run inside an event loop (e.g. `asyncio.run` or via `await`).

---

## 🏠 Real-life analogy — Regular chef vs special chef

- Normal function:
  - Chef cooks a dish start to finish immediately 🍲
- `async` function:
  - Chef can start cooking, pause while waiting (boiling, baking), work on other dishes, and resume later

`async` = giving the chef the ability to multitask efficiently.

---

## 💡 Key behavior change

- Without `async`:
  - Function runs immediately, cannot pause, blocks execution.
- With `async`:
  - Function is pausable; execution is controlled externally by an event loop.

---

## 🔄 What happens when you call a coroutine

```python
async def foo():
    return 10

coro = foo()  # returns a coroutine object; not executed
```

To run it you need:
- `await foo()` inside another async function, or
- `asyncio.run(foo())` from synchronous code

---

## 🚀 Why `async` is needed

- Without `async`: Python treats everything as blocking — no cooperative pausing.
- With `async`: Enables non-blocking I/O and concurrency via an event loop.

---

## 📌 What `async` enables

1. ⏸️ `await` — pause execution without blocking the whole thread  
2. 🔄 Coroutines — functions that can resume later  
3. ⚡ Event loop integration — scheduling and cooperative concurrency

---

## ⚠️ Important insight
- `async` alone does **not** make code asynchronous.
- It only marks a function as *capable* of being paused.
- You still need `await` and an event loop (e.g., `asyncio`) to run coroutines.

---

## 🧠 Mental model

| Without `async` | With `async` |
|---|---|
| Normal function | Coroutine function |
| Runs immediately | Runs when scheduled |
| Blocking | Non-blocking capable |

---

## 🔁 Quick recap
- `async` makes a function a coroutine function.
- It enables pause/resume behavior.
- Calling it returns a coroutine object — it does not run immediately.
- Coroutines must be executed with `await` or an event loop.
- Core building block of async programming.

---

## 🔜 Next step
What does `await` keyword do?
