# Lock vs Semaphore (Comparison)

## ❓ Basic Question
**What is the difference between a Lock and a Semaphore in async Python?**

---

## 🧠 Simple Answer

👉 Both are used for synchronization, but:

- **Lock** → only **1 task** allowed at a time  
- **Semaphore** → **N tasks** allowed at a time  

---

## ⚙️ Core Idea

| Tool | Purpose |
|------|--------|
| Lock | Full exclusive access |
| Semaphore | Limited shared access |

👉 Lock is strict, Semaphore is flexible


## 🔒 Lock (Mutual Exclusion)

### Behavior:
- Only one task can enter
- Others must wait

```python
async with lock:
    # only one task runs here
```

- Use when:
    - Modifying shared data
    - Critical sections must not overlap

## 🚦 Semaphore (Limited Concurrency)

### Behavior:
- Allows multiple tasks (fixed number)
- Extra tasks wait
```python
async with semaphore:
    # limited number of tasks run here
```
- Use when:
    - Limiting API calls
    - Controlling resource usage
    - Rate limiting

## 🏠 Real-Life Analogy

### 🚿 Bathroom vs 🚪 Room
```
Lock → single bathroom 🚿 → only one person at a time (Semaphore) → room with 3 seats 🚪 → 3 people allowed together
```

## 🧠 Mental Model
- Lock = strict gate (1 entry)
- Semaphore = controlled gate (N entries)

## ⚠️ Common Mistakes
- ❌ Using Lock when Semaphore is needed
    - reduces performance unnecessarily
- ❌ Using Semaphore for critical data
    - can still cause data issues if multiple tasks modify data

## 🔥 Best Practices
- Use Lock when:
    - You need complete safety
    - Only one task must access resource
- Use Semaphore when:
    - You want controlled parallelism
    - System can handle limited concurrency

## 📊 Summary Table
| Feature        | Lock                   | Semaphore              |
|----------------|------------------------|------------------------|
| Allowed tasks  | 1                      | N                      |
| Purpose        | Exclusive access       | Limit concurrency      |
| Use case       | Shared data protection | Rate limiting          |
| Strictness     | High                   | Flexible               |

## 🔁 Quick Recap
- Lock → only one task at a time
- Semaphore → multiple tasks with a limit
- Lock for safety, Semaphore for control