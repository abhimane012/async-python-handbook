# Does `gather()` Stop on Error?

## ❓ Basic Question
**If one task fails inside `asyncio.gather()`, does it stop the other tasks or continue running them?**

---

## 🧠 Simple Answer

👉 By default, yes — `gather()` *fails fast*.

- It raises an exception as soon as one task fails
- The whole `gather()` call is considered failed

BUT:
- Other tasks may still be running internally
- You just don’t reliably get their results


## ⚙️ Core Idea

`asyncio.gather()` has two important behaviors:

### 1. Default behavior (no options)
- First exception is raised immediately
- Remaining results are discarded from your perspective
- Whole operation is marked as failed


### 2. Controlled behavior

```python
await asyncio.gather(task1(), task2(), task3(), return_exceptions=True)
```
- No early stop
- All tasks finish
- Errors are returned as values instead of crashing

#### 🧵 What Actually Happens Internally?

- Even when gather() "fails fast":
    - Tasks are already scheduled
    - Some may continue running briefly
    - But Python does not wait for clean completion of all results before raising error

👉 So:
- It behaves like “fail fast reporting”
- Not strict “stop all execution instantly”

## 🏠 Real-Life Analogy

### 📦 Group Delivery System

- You order:
    - Pizza 🍕
    - Burger 🍔
    - Sushi 🍣

- If pizza fails:
    - Default gather():
        - 🚨 System immediately reports failure
        - 📦 Other deliveries may still be in progress
        - ❌ But system treats whole order as failed
    - With `return_exceptions=True`:
        - 📦 All deliveries complete
        - 📋 You get a report of what failed and what succeeded

## ⚠️ Common Misunderstanding

### ❌ “gather stops all tasks immediately”

> Not exactly.

### Correct understanding:

- It raises error immediately
- But does not guarantee instant cancellation of all tasks

## 🔥 Best Practice
- Use default gather() when:
    - You want strict behavior
    - Any failure should stop the process
- Use `return_exceptions=True` when:
    - Partial success is acceptable
    - You want all results (success + failure)

## 📊 Summary
| Behavior                          | What happens                                  |
|----------------------------------|-----------------------------------------------|
| Default gather()                 | Raises error immediately                      |
| Tasks inside gather()            | May still run briefly                         |
| return_exceptions=True           | No crash, all results returned                |

## 🔁 Quick Recap
- `gather()` does not truly “kill everything instantly”
- It raises errors immediately
- Default behavior = fail fast
- Use `return_exceptions=True` for resilience