# When Does a Coroutine Actually Run?

## ❓ Basic Question
**If I call a coroutine in Python, when does it actually execute? Immediately or later?**

---

## 🧠 Simple Answer

👉 A coroutine does NOT run when you call it.

It only runs when it is:
> scheduled and controlled by the event loop (usually via `asyncio`)

---

## ⚙️ Key Idea

When you call a coroutine:

- It is created first
- It stays idle (paused state)
- It runs only when the event loop starts executing it

---

## 🏠 Real-Life Analogy

### 📋 Restaurant Order Ticket

- You write an order (coroutine is created)
- You hand it to the kitchen (event loop)
- Chef decides when to start cooking
- You don’t start cooking the moment order is written

👉 Writing order ≠ cooking starts

---

## 💡 Step-by-Step Flow (No Code)

### 1. You define coroutine
- A function marked with `async def`

---

### 2. You call it
- Python creates a coroutine object
- BUT nothing runs yet

👉 It’s just a “ready task”

---

### 3. Event loop receives it
- You pass it to `asyncio.run()` or `create_task()`

---

### 4. Event loop starts execution
- Now coroutine begins running
- It executes until it hits `await`

---

### 5. Coroutine pauses if needed
- On `await`, it gives control back to event loop
- Event loop runs other tasks

---

### 6. Coroutine resumes later
- When awaited result is ready
- Event loop resumes it from same point

---

## 🚨 Important Insight

👉 Calling a coroutine does NOT execute it  
👉 Only the event loop executes it

---

## 🧠 Simple Mental Model

| Action                  | What happens |
|------------------------|-------------|
| `async def function()` | Defines coroutine |
| `function()` call      | Creates coroutine object |
| `asyncio.run()`        | Starts event loop |
| Event loop             | Actually runs coroutine |

---

## 🏠 Real-Life Analogy (Better Version)

### 🎬 Movie Production

- Writing script = coroutine definition
- Booking actor = calling coroutine
- Director starts filming = event loop
- Scenes shot over time = coroutine execution
- Pauses between scenes = `await`

👉 The movie doesn’t start just because script is written

---

## ⚡ When EXACTLY does it run?

A coroutine runs only when:

- It is passed to an event loop
- OR wrapped in a Task
- OR awaited inside another coroutine running in event loop

---

## 📌 Common Mistake

### ❌ Wrong assumption:
> “I called async function, so it ran”

### ✅ Correct understanding:
> “I created a coroutine object, but it runs only inside event loop”

---

## 🔥 Key Insight

👉 Coroutines are **lazy execution units**  
👉 They wait for the event loop to schedule them

---

## 🔁 Quick Recap

- Calling a coroutine does NOT run it
- It only creates a coroutine object
- Event loop is responsible for execution
- It runs, pauses, and resumes coroutines
- Execution happens only when scheduled by asyncio

---

## 🔜 Next Step

Now the next important concept is:

👉 **Can we call a coroutine like a normal function?**