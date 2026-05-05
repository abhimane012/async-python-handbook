# Can We Call a Coroutine Like a Normal Function?

## ❓ Basic Question
**Can we call a coroutine (`async def`) like a normal function and expect it to run immediately?**

---

## 🧠 Simple Answer

👉 You can call it, but it will NOT behave like a normal function.

Instead of running, it will return a:
> coroutine object (a “paused task”)

To actually run it, you need:
> an event loop (like `asyncio.run()` or `await`)

---

## ⚙️ Key Idea

| Action | Result |
|--------|--------|
| Call normal function | Executes immediately |
| Call coroutine function | Returns coroutine object (does NOT run) |

---

## 🏠 Real-Life Analogy

### 📦 Ordering Food

- Normal function = you eat immediately 🍔
- Coroutine = you place an order ticket 🧾

👉 Just placing the order does NOT give you food  
👉 Kitchen (event loop) must process it first

---

## 💡 What Happens Internally

When you do this:

- `func()` where `func` is a coroutine

Python:
- does NOT execute it
- creates a coroutine object
- waits for event loop to run it

---

## 🚫 Common Mistake

### ❌ Wrong assumption:
> “I called async function, so it ran”

### 🧠 Reality:
> “I created a coroutine object, but it is not executed yet”

---

## 🔄 How to Actually Run a Coroutine

You need one of these:

### 1. `asyncio.run()`
- Starts event loop
- Runs coroutine
- Closes loop

---

### 2. `await`
- Used inside another coroutine
- Pauses and resumes execution

---

### 3. `asyncio.create_task()`
- Schedules coroutine to run in background
- Event loop manages it

---

## 🏠 Real-Life Analogy (Better Understanding)

### 🎬 Theater Example

- Normal function = actor performs live immediately
- Coroutine = actor waits backstage

👉 Actor does NOT perform until director (event loop) calls them on stage

---

## ⚡ Key Insight

👉 Calling a coroutine is like **creating a plan**, not executing it.

Execution happens only when:
- event loop schedules it
- or it is awaited

---

## 📌 Why Python Works This Way

Because coroutines are designed for:

- non-blocking execution
- controlled scheduling
- concurrency via event loop

If they ran immediately:
- async system would break
- blocking would happen again

---

## 🔁 Quick Recap

- Yes, you can call a coroutine like a function
- But it does NOT execute immediately
- It returns a coroutine object
- Event loop or `await` is required to run it
- This design enables async programming

---