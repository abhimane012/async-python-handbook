# What is an Event Loop?

## ❓ Basic Question
**What is an event loop and why is it important in async programming?**

---

## 🧠 Simple Explanation

An event loop is a system that **keeps checking for tasks and runs them when they are ready**, instead of waiting idly.

👉 In simple words:
> “It is a loop that decides which task to run next.”

---

## 🏠 Real-Life Analogy

### 🧑‍🍳 Restaurant Order Counter

Imagine a chef and an order counter:

- Customers place orders 🍔
- Some orders take time (like baking)
- Instead of waiting, the chef:
  - checks which orders are ready
  - starts new ones
  - serves finished ones

👉 The chef keeps **looping between tasks**

That “checking and switching continuously” is like an event loop.

---

## ⚙️ Technical Explanation (Simple)

The event loop is a core part of async systems.

It does 3 main things:

### 1. 📥 Takes tasks
- Receives async tasks (like API calls, file reads)

### 2. ⏳ Waits for completion (without blocking)
- Lets tasks run in the background

### 3. 🔔 Executes ready tasks
- When a task finishes, it runs the next step (callback / continuation)

---

## 🔄 How It Works (Simple Flow)

1. Start Task A (API call)
2. Start Task B (file read)
3. Event loop does NOT wait
4. It keeps checking:
   - Is Task A done?
   - Is Task B done?
5. When a task is done → run its handler
6. Repeat forever

👉 That continuous checking cycle = event loop

---

## 💡 Key Idea

👉 The event loop is like a **manager**:

- It does NOT do heavy work itself
- It only:
  - schedules tasks
  - switches between them
  - runs them when ready

---

## 🚀 Why Event Loop is Important

Without an event loop:

- async programming cannot work
- tasks would block each other
- system would behave like normal sequential code

With event loop:

- multiple tasks can progress together
- system stays responsive
- efficient use of CPU time

---

## 📌 Where You See Event Loops

### 🌐 Web servers
- Handle thousands of requests efficiently

### 🧠 JavaScript runtime (browser / Node.js)
- Handles UI events, API calls, timers

### 🐍 Python asyncio
- Manages async tasks using `asyncio` event loop

---

## ⚠️ Important Insight

👉 The event loop does NOT run tasks in parallel  
👉 It switches between tasks very quickly

So it enables:
- concurrency
- not necessarily parallel execution

---

## 🔥 Simple Mental Model

Think of it like:

> A smart worker who keeps checking:  
> “Who is ready now?” → then handles that task → repeats forever

---

## 🔁 Quick Recap

- Event loop manages async tasks
- It continuously checks for completed tasks
- Runs tasks when they are ready
- Enables non-blocking and concurrent programming
- Core of async systems like Python asyncio

---

## 🔜 Next Step

Now that you understand the event loop:

👉 **Why is event loop needed?**