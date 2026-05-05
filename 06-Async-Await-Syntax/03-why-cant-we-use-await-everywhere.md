# Why Can't We Use `await` Everywhere?

## ❓ Basic Question
**If `await` is so useful, why can’t we just use it in any line of Python code?**

---

## 🧠 Simple Answer

👉 You can only use `await` inside an **async function** because:

> `await` needs an event loop context to pause and resume execution.

Outside that context, Python has no mechanism to “pause and come back later”.

---

## ⚙️ Core Rule

```text
await can only be used inside async def
```

### 🏠 Real-Life Analogy — Theater Performance
- async function = a stage performance  
- event loop = director managing timing  
- await = actor pausing a scene and waiting for a cue

👉 You can only pause properly if:
- you're already on stage
- the director is managing timing

If you're just in the audience (a normal function), you can't “pause and resume the performance”.

---

## 💡 What Happens If You Try `await` Everywhere?

Example (invalid):

```python
# Outside async function — this raises a SyntaxError
await some_task()
```

👉 Python will give an error:

```
SyntaxError: 'await' outside async function
```

---

## 🧠 Why Python Restricts This

Because `await` depends on:

1. 🔄 Event loop — There must be a running loop to resume execution.  
2. 📍 Coroutine context — Python must know where to pause and resume.  
3. 🧵 Controlled execution flow — Only async functions are managed by the event loop.

---

## 🚫 Why Normal Functions Can’t Use `await`

Normal functions:
- run top to bottom
- cannot pause mid-way
- are not managed by an event loop

So if you write:

```python
def normal_function():
    await something()
```

Python has no idea:
- where to pause
- who will resume it
- which event loop is managing it

---

## 🔄 Key Idea

| Context         | Can use await? | Why                         |
|-----------------|----------------|-----------------------------|
| async function  | ✅ Yes         | Managed by event loop       |
| normal function | ❌ No          | No async control system     |

### 🏠 Real-Life Analogy (Better Version) — Customer Support System
- Async function = agent on the call system  
- Event loop = call manager  
- await = putting a call on hold and switching tasks

👉 Only agents inside the system can put calls on hold. Random people outside cannot.

---

## ⚡ Important Insight

👉 `await` is not just a keyword — it is a coordination mechanism with the event loop.

Without that system:
- nothing can resume execution
- the async model breaks

---

## 🔥 Key Takeaway

You can only pause execution (`await`) if there is a system that knows how to resume it (the event loop).

---

## 🔁 Quick Recap
- `await` only works inside `async def`.  
- It needs an event loop to function.  
- Normal functions cannot pause/resume execution.  
- Python restricts it to maintain safe async behavior.  
- It is tightly bound to the coroutine execution model.

---

## 🔜 Next Step

Now that you understand `await` deeply:

👉 What happens if we forget `await` ?