# Difference Between Generator and Async Generator

## ❓ Basic Question
**What is the difference between a normal generator and an async generator in Python?**

---

## 🧠 Simple Answer

👉 Both generate values using `yield`, but:

- **Generator** → produces values immediately  
- **Async Generator** → produces values over time (can wait)


## ⚙️ Core Idea

| Feature | Generator | Async Generator |
|--------|----------|-----------------|
| Definition | `def` | `async def` |
| Yield values | Yes | Yes |
| Can use `await` | ❌ No | ✅ Yes |
| Data availability | Immediate | Delayed |
| Loop type | `for` | `async for` |

---

### 🧵 1. Generator

```python
def gen():
    yield 1
    yield 2
```
- Behavior:
    - Values are ready instantly
    - No waiting involved
    - Used with normal for

### 🧵 2. Async Generator
```python
async def gen():
    yield 1
    await something()
    yield 2
```

- Behavior:
    - Can pause using await
    - Values may come slowly
    - Used with async for

## 🚨 Key Difference
- Generator → synchronous, immediate data
- Async generator → asynchronous, delayed data

## 🏠 Real-Life Analogy
### 📦 vs 🚰
- Generator → box of items ready 📦
- Async generator → water flow over time 🚰

## 🧠 Mental Model
- Generator = instant producer
- Async generator = time-based producer

## ⚠️ Common Mistakes
- ❌ Using for with async generator
    - Must use async for
- ❌ Using await in normal generator
    - Not allowed
- ❌ Expecting async behavior from normal generator
    - It does not wait

## 🔥 Best Practices

- Use generator when:
    - Data is already available
    - No async operations needed
- Use async generator when:
    - Data comes from I/O
    - You need to await between yields

## 📊 Summary
| Use Case          | Generator | Async Generator |
|-------------------|-----------|-----------------|
| Ready data        | ✅        | ❌              |
| Streaming data    | ❌        | ✅              |
| Needs await       | ❌        | ✅              |
| Simple iteration  | ✅        | ❌              |

## 🔁 Quick Recap
- Both use yield
- Generator → immediate values
- Async generator → delayed values with await
- Use for vs async for accordingly