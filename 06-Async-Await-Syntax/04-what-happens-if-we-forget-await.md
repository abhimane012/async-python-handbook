# What Happens Internally if We Forget `await`?

## ❓ Basic Question
**If I call an async function but forget to use `await`, what actually happens inside Python?**

---

## 🧠 Simple Answer

👉 If you forget `await`, the coroutine is **created but never executed**.

So instead of running your async task, Python just gives you a:
> coroutine object (a “paused task”) that nobody is driving

---

## ⚙️ Core Idea

```python
result = some_async_function()

# If some_async_function is async:
# - It does NOT run
# - It returns a coroutine object
# - Event loop does NOT automatically execute it
```

## 🏠 Real‑Life Analogy

### 📦 Food Order Example
You place an order 🍔  
But you never give it to the kitchen.

👉 So:
- Order exists  
- But food is never cooked

That “unprocessed order” = coroutine without `await`

## 💡 What Actually Happens Step‑by‑Step
1. You call async function — Python creates a coroutine object  
2. You forget `await` — No event loop scheduling happens  
3. Coroutine sits idle — It is never executed  
4. Program continues — Nothing blocks, but also nothing happens

## 🚨 Important Behavior

Python will NOT automatically warn you in many cases. Instead:
- coroutine is silently created  
- not executed  
- may trigger warning later

Example warning:

> RuntimeWarning: coroutine was never awaited

## 🧠 Mental Model

| With await | Without await |
|---|---|
| Coroutine runs | Coroutine is created only |
| Task executes | Task does nothing |
| Result returned | No result |
| Event loop involved | Event loop unused |

## ⚠️ Why This is a Big Problem

Forgetting `await` causes:
1. ❌ Code not executing — Your async logic never runs  
2. 🐛 Silent bugs — No crash immediately, but missing behavior  
3. 📉 Unexpected behavior — APIs not called, DB not updated, tasks silently ignored

## 💡 Real‑World Example

You want to send an email asynchronously:

```python
send_email(user)      # If send_email is async and you forget await:
                      # Email is never sent 📭
                      # No immediate error — system looks fine but fails logically
```

Correct usage:

```python
await send_email(user)
```

## 🚀 Key Insight

👉 `await` is what connects the coroutine to the event loop. Without it:
- The coroutine exists, but it is never scheduled or executed

## 🔥 Simple Rule

If it's async, and you don't `await` it → it does NOT run

## 🔁 Quick Recap
- Forgetting `await` does NOT run the coroutine  
- It only creates a coroutine object  
- Event loop is never triggered for it  
- Leads to silent bugs and missing behavior  
- Python may show a warning, but not always

---
