# Why Do We Need Locks If Async Is Single-Threaded?

## ❓ Basic Question
**If async Python runs in a single thread, why do we still need locks?**

---

## 🧠 Simple Answer

👉 Because async tasks can **pause (`await`) and let other tasks run**.

Even in a single thread:
- Tasks can **interleave**
- Shared data can still be **modified at the wrong time**

👉 Locks are needed to prevent this kind of interference.

---

## ⚙️ Core Idea

Async is:
- Single-threaded ✅
- But **concurrent** ❗

This means:
- Only one task runs at a time
- BUT tasks switch during `await`

👉 That switch can break logic if multiple tasks touch the same data.

---

## 🧵 Where Problems Happen

### Example idea:
- Two tasks updating same variable:

    ```python
    x = x + 1
    ```

- Looks safe… but internally:

    - Read x
    - Add 1
    - Write back

- If a task pauses between steps:
    - Another task may change x
    - Final value becomes incorrect

- 👉 This is a race condition


## 🔒 How Lock Solves This

- A lock ensures:

    - Only one task enters critical section
    - Others must wait
        ```python
        async with lock:
            # safe operation
        ```
👉 No interruption happens inside this block

## 🧠 Mental Model

- Threading issue → multiple threads
- Async issue → multiple interleaving tasks

👉 Problem is different, but result (data corruption) is similar

## 🏠 Real-Life Analogy

### 📝 Shared Notebook

- Two people writing in the same notebook:

    - Without lock → both write at same time → messy ❌
    - With lock → one writes, others wait ✅

Even if they take turns quickly, overlap can still happen.

## ⚠️ Common Misunderstandings

❌ “Single-threaded means no problems”

- Wrong — concurrency still exists

❌ “Only threads need locks”

- Async tasks also need coordination

❌ “No await = safe”

- Only safe if NO await inside critical logic

## 🔥 Best Practices

### 1. Use locks when modifying shared state
- variables
- files
- shared objects

### 2. Keep critical section small
```python
async with lock:
    update()
```

### 3. Avoid unnecessary locking
- too many locks reduce performance

## 📊 Summary
| Concept        | Reality                         |
|----------------|---------------------------------|
| Async model    | Single-threaded                 |
| Execution      | Concurrent (via await)          |
| Problem        | Task interleaving               |
| Solution       | Locks for safety                |

## 🔁 Quick Recap
- Async is single-threaded but concurrent
- Tasks switch at await
- This can cause race conditions
- Locks prevent unsafe access to shared data
