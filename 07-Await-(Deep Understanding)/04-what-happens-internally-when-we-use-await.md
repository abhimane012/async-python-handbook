# What Happens Internally When We Use `await`?

## ❓ Basic Question
**When Python hits `await`, what is actually happening under the hood?**

---

## 🧠 Simple Answer

👉 When you use `await`, Python:
> pauses the current coroutine, registers what it is waiting for, and hands control back to the event loop.

The event loop then continues running other tasks and later resumes your coroutine.

---

## ⚙️ High-Level Internal Flow

When Python executes:

```python
result = await some_awaitable()
```

this is what happens internally:

1. 🔍 Coroutine reaches `await`  
    - Execution starts normally inside the coroutine.  
    - It runs line by line and then hits `await`.

2. 📦 Awaitable is identified  
    - Python checks: Is this object awaitable? Does it have `__await__()`?  
    - If yes → continue async handling.

3. ⏸️ Coroutine is suspended  
    - Current coroutine state is paused.  
    - Stack frame is saved (so it can resume later).  
    - Execution stops here (only for this coroutine).  
    - 👉 Important: nothing is lost, everything is stored.

4. 🔄 Control is returned to the event loop  
    - Event loop is notified: “This coroutine is waiting for X”.  
    - Coroutine is moved to a “waiting” state.

5. ⚡ Event loop runs other tasks  
    - While your coroutine is waiting: other coroutines run, completed tasks are processed, new tasks are scheduled.  
    - 👉 CPU is not idle.

6. 🔔 Awaitable completes  
    - When the awaited operation finishes, the result becomes available and the event loop gets a notification.

7. 🔁 Coroutine resumes  
    - Saved state is restored.  
    - Execution continues from the exact line after `await`.  
    - Example: `result = await some_task()` — resumes here after completion.

---

## 🏠 Real-Life Analogy

🍳 Chef in a busy kitchen  
- Chef starts cooking pasta 🍝.  
- Pasta needs boiling → chef pauses this dish and moves to other dishes 🥗.  
- Pasta is ready → chef comes back and continues plating.  

👉 Nothing is “lost”, just paused and resumed.

---

## 🧠 Mental Model
```
start coroutine  
    ↓  
run code  
    ↓  
hit await → pause ⏸️  
    ↓  
event loop runs other tasks 🔄  
    ↓  
awaitable completes 🔔  
    ↓  
resume coroutine 🔁
```
---

## 🚨 Important Insight

- 👉 `await` does NOT create a new thread.  
- 👉 It does NOT block the program.  
- 👉 It only “pauses + resumes” execution flow.

---

## ⚡ What Makes This Efficient

- no thread switching overhead  
- no blocking CPU  
- one thread can handle many tasks  
- ideal for I/O-heavy work

---

## 📌 Key Takeaway

👉 `await` is a pause-and-resume mechanism controlled by the event loop.  
It is not magic execution — it is: state saving, task switching, event-driven resumption.

---

## 🔁 Quick Recap

- `await` pauses only the current coroutine  
- event loop takes control  
- other tasks run in the meantime  
- coroutine resumes when result is ready  
- execution continues from the same point

---

