# What Happens If One Task Fails?

## ❓ Basic Question
**What happens in async Python if one task fails while others are running?**

---

## 🧠 Simple Answer

👉 One task failing does not always break everything.

It depends on how tasks are run:
- `await`
- `asyncio.create_task()`
- `asyncio.gather()`

Each handles failure differently.


## ⚙️ Core Idea

- Each async task runs independently
- Each task can fail on its own
- The way you manage tasks decides the impact of failure


### 1. 🟢 `asyncio.gather()` (Default Behavior)

```python
await asyncio.gather(task1(), task2(), task3())
```
- If one task fails:
    - ❌ gather() raises an exception
    - 🛑 Remaining tasks may not complete
    - ❌ Entire operation is considered failed
    - 🔧 With return_exceptions=True

```python   
await asyncio.gather(task1(), task2(), task3(), return_exceptions=True)
```

- Behavior:
    - All tasks complete
    - Errors are returned as values instead of being raised

### 2. 🧵 asyncio.create_task()
```python
t1 = asyncio.create_task(task1())
t2 = asyncio.create_task(task2())
```
- If one task fails:
    - ❌ Exception is stored inside that task
    - 🟡 Other tasks keep running

- Important:
    - If you don’t await or inspect the task, errors may be missed
    - ```python 
        await t1
      ```

### 3. 🟢 Direct await
```python
await task1()
```

- If it fails:
    - ❌ Exception is raised immediately
        - Only that task is affected

## 🏠 Simple Analogy
- await → single order fails immediately 🚨
- create_task() → one order fails, others continue 📦
- gather() → all orders fail together by default ❌📦📦

## ⚠️ Common Mistakes
- Assuming one task failure always breaks everything
- Ignoring exceptions from created tasks
- Not using return_exceptions when partial success is needed

## 📊 Summary
| Method                                   | If One Task Fails                          |
|------------------------------------------|---------------------------------------------|
| await                                    | Fails immediately for that task            |
| create_task()                            | Failure stored, others continue            |
| gather()                                 | Fails entire group (default)               |
| gather(return_exceptions=True)           | All complete, errors returned              |


## 🔁 Quick Recap
- Tasks fail independently
- Impact depends on execution method
- gather() is strict by default
- create_task() is isolated
- await is immediate

## 🔜 Next Step

👉 Does gather() stop on error?