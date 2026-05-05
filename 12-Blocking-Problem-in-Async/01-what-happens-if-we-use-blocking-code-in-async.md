# What Happens If We Use Blocking Code in Async?

## ❓ Basic Question
**If async is non-blocking, what happens when we accidentally use blocking code inside async functions?**

---

## 🧠 Simple Answer

👉 If you use blocking code inside async:
> **it blocks the entire event loop**

This means:
- all other tasks stop
- concurrency is broken
- performance drops

---

## ⚙️ Core Idea

Async works only when tasks:
- pause using `await`
- allow the event loop to switch tasks

👉 Blocking code does NOT pause  
👉 It **holds the thread completely**

---

## 🏠 Real-Life Analogy

### 👨‍🍳 Kitchen Problem

- Chef is handling many dishes (async tasks)

#### Normal async:
- Rice cooks 🍚 → chef works on curry 🍛

---

#### With blocking:
- Chef stands doing ONE task 😐
- Ignores all other dishes

👉 Everything slows down

---

## 🔄 What Actually Happens Internally

1. Event loop runs a coroutine
2. Coroutine calls blocking code
3. That code:
   - does NOT use `await`
   - does NOT yield control
4. Event loop is stuck
5. No other task runs

---

## 🚫 Example Idea (No Code)

Using:

- `time.sleep()` (blocking)

Instead of:

- `asyncio.sleep()` (non-blocking)

👉 `time.sleep()` freezes everything

---

## ⚠️ Effects of Blocking Code in Async



### 1. ❌ No Concurrency

- tasks cannot switch
- everything becomes sequential

---

### 2. 🐌 Performance Drops

- waiting time is wasted
- system becomes slow

---

### 3. ⛔ Event Loop Freeze

- entire async system pauses

---

### 4. 🚨 Bad User Experience

- slow APIs
- delayed responses

---

## 📊 Blocking vs Non-Blocking in Async

| Behavior | Blocking Code | Async Code |
|--------|--------------|-----------|
| Uses `await` | ❌ No | ✅ Yes |
| Allows switching | ❌ No | ✅ Yes |
| Blocks event loop | ✅ Yes | ❌ No |
| Concurrency | ❌ Broken | ✅ Works |

---

## 🚨 Common Mistakes


### ❌ Using blocking libraries

- `requests` (HTTP)
- `time.sleep()`
- heavy sync DB calls

---

### ✅ Use async alternatives

- `aiohttp`, `httpx`
- `asyncio.sleep()`
- async DB drivers

---

## 🧠 Mental Model

### Async + blocking code = broken async

## 🔥 Key Takeaway

👉 One blocking call can stop your entire async system

## 🔁 Quick Recap
- Blocking code freezes event loop
- No task switching happens
- Concurrency is lost
- Performance degrades
- Always use async-compatible libraries

🔜 Next Step

👉 Why does time.sleep() break async?