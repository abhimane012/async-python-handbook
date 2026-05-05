# What is `asyncio.gather()`?

## ❓ Basic Question
**How do we run multiple async tasks together and get all their results easily?**

---

## 🧠 Simple Answer

👉 `asyncio.gather()` is used to:
> run multiple awaitables **concurrently** and collect all their results together

---

## ⚙️ Core Idea

Instead of writing:

```python
await task1()
await task2()
await task3()
```

👉 which runs sequentially

You use:
```python
await asyncio.gather(task1(), task2(), task3())
```

👉 which runs them concurrently

## 🏠 Real-Life Analogy

### 🍳 Kitchen Example
 - You need:
   - rice 🍚
   - curry 🍛
   - salad 🥗
- Without gather:
   - cook rice → wait
   - cook curry → wait
   - make salad → wait
- With gather:
   - start all dishes together
   - wait for all to complete

👉 Everything finishes faster

## 🔄 What Happens Internally

### When you use gather():

 - Takes multiple awaitables
    - Converts them into Tasks (if not already)
    - Schedules all on event loop
    - Runs them concurrently
 - Waits for ALL to complete
 - Returns results in order
 - 📦 Return Value
results = await asyncio.gather(a(), b(), c())

👉 results will be:

[result_of_a, result_of_b, result_of_c]

- ✔ Order is preserved
- ✔ Even if execution order is different

## 🚀 Why Use gather()?
1. ⚡ Run multiple tasks concurrently
   - API calls
   - DB queries
   - file operations
2. 📦 Collect results easily
   - No need to await each task separately
3. 🧼 Cleaner code
   - More readable than multiple awaits

## ⚠️ Important Behavior

### 🔥 If one task fails:
 - By default → gather() raises exception
 - Other tasks may still run
 - Optional behavior:
   - You can handle errors differently (advanced)

## 🧠 Mental Model

#### gather() → start all tasks → wait for all → return results

---

## 🔄 gather vs create_task

| Feature | gather() | create_task() |
|--------|----------|--------------|
| Purpose | run & collect results | run in background |
| Waits for completion | ✅ Yes | ❌ No (unless awaited) |
| Returns results | ✅ Yes | ❌ Not directly |
| Use case | batch execution | background work |

---

## 🏠 Real-Life Analogy (Better Version)

### 📦 Package Delivery

- `create_task()` = send packages independently 🚚
- `gather()` = send multiple packages AND wait for all deliveries 📦📦📦

---

## 🚨 Common Mistake

### ❌ Wrong idea:
> “gather is same as multiple awaits”

### ✅ Correct:
> “gather runs tasks concurrently, not sequentially”

---

## 🔥 Key Takeaway

👉 Use `asyncio.gather()` when you want:

- multiple async operations
- to run together
- and collect all results at once

---

## 🔁 Quick Recap

- Runs multiple awaitables concurrently
- Waits for all to complete
- Returns results in order
- Simplifies async code
- Essential for parallel-style async execution

---

## 🔜 Next Step

👉 Difference between sequential vs concurrent execution??