# Why Does `time.sleep()` Break Async?

## ❓ Basic Question
**Why does using `time.sleep()` inside async code cause problems?**

---

## 🧠 Short Answer

👉 `time.sleep()` **blocks the entire thread**, so the event loop cannot run anything else.

---

## ⚙️ What Makes It Problematic

`time.sleep()`:
- pauses execution at the OS/thread level
- does NOT give control back to the event loop
- freezes everything running on that thread

---

## 🔄 What Actually Happens

Inside async code:

1. Coroutine starts running
2. Hits `time.sleep(2)`
3. Python thread goes to sleep
4. Event loop cannot run
5. All other tasks are stuck

---

## 📉 Practical Effect

Even if multiple tasks are scheduled:

```
Task A → time.sleep()
Task B → waiting
Task C → waiting
```

👉 Nothing progresses until sleep finishes

## ⚖️ Compare with `asyncio.sleep()`
- `time.sleep()`
    - blocks thread
    - stops event loop
    - no task switching
- `asyncio.sleep()`
    - pauses only current coroutine
    - allows event loop to run others
    - enables concurrency

## 🧠 Mental Model
- `time.sleep()` → "stop everything"
- `asyncio.sleep()` → "pause me, continue others"

## 🔥 Key Takeaway

- 👉 `time.sleep()` breaks async because it does not cooperate with the event loop.
- 👉 Async code requires operations that yield control, not block it.

## 🔜 Next Step
- 👉 How can we safely run blocking functions inside async code?