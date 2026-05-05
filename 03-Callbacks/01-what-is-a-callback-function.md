# What is a Callback Function?

## ❓ Basic Question
**What is a callback function and why do we need it in programming?**

---

## 🧠 Simple Explanation (No Jargon)

A callback function is a function that you **pass to another function**, and it gets **called later when needed**.

👉 In simple words:
> “I’ll give you a function, and you call it when the time is right.”

---

## 🏠 Real-Life Analogy

### 📞 Food Delivery Example

- You order food 🍔
- You give your phone number
- You say: “Call me when food arrives”

👉 You don’t keep checking every minute  
👉 You **wait for a callback (call from delivery guy)**

That “call when ready” is a callback idea.

---

## ⚙️ Slightly Technical Explanation

In programming:

- A function is passed as an argument to another function
- The second function decides **when to execute it**
- It is “called back” after some operation completes

---

## 💡 Simple Example Idea (No Code)

Imagine a program:

- Function A: “Download file”
- Function B: “Show success message”

You pass Function B into Function A:

- Start download
- When download finishes → call Function B

👉 Function B is the **callback**

---

## 🚀 Why Callbacks Are Used

Callbacks help you:

- ⏳ Run code after a task finishes
- 🌐 Handle asynchronous operations (like API calls)
- 🔄 React to events (clicks, responses, timers)
- 🧩 Keep code modular and flexible

---

## 📌 Real-World Where You See Callbacks

- 🌐 API responses in web apps
- 🖱️ Button click handlers in UI apps
- ⏱️ Timers (`run after 5 seconds`)
- 📡 Network request completion handlers

---

## ⚠️ Important Idea

👉 The function you pass is **not executed immediately**  
👉 It is executed **later by another function**

---

## 🔥 Simple Mental Model

Think of callbacks like:

> “Here is what to do… call me when done.”

---

## 🔁 Quick Recap

- Callback = function passed into another function
- It runs later, not immediately
- Used for async tasks, events, and delayed execution
- Helps make programs flexible and responsive

---

## 🔜 Next Step

Now the next concept that builds on this is:

👉 **Why were callbacks used before async/await?**