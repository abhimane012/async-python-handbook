# What is an Async Generator?

## ❓ Basic Question
**What is an async generator in Python, and how is it different from a normal generator?**

---

## 🧠 Simple Answer

👉 An async generator is:
> A function that **produces values over time asynchronously** using `yield`.

It combines:
- async behavior (`async`)
- generator behavior (`yield`)


## ⚙️ Core Idea

- Normal generator:
```python
def gen():
    yield 1
```

- Async generator:
```python
async def gen():
    yield 1
```

👉 Key difference:

- Async generator can pause with await
- Values are produced over time, not instantly

## 🧵 How It Works
- Defined using async def
- Uses yield to produce values
- Can use await inside

👉 It creates an asynchronous data source

## 🧪 Example Idea
- Fetch data from API step by step
- Yield each result as it arrives
- Fetch → wait → yield → repeat

## 🔁 How to Use It

You cannot use normal for loop.

Instead:

```python
async for item in gen():
    ...
```

👉 Because values are not ready immediately

## 🚨 Key Behavior
- Produces values one by one
- May wait between values (await)
- Works with async for

## 🏠 Real-Life Analogy
### 🚰 Water Dispenser
- Water doesn’t come all at once
- It flows gradually

👉 Async generator = controlled flow of data

## 🧠 Mental Model
- Generator = value producer 📦
- Async generator = delayed value producer ⏳

## ⚠️ Common Mistakes
- ❌ Using normal for
    - async generators need async for
- ❌ Forgetting await inside
    - defeats async purpose
- ❌ Expecting instant values
    - values arrive over time

## 🔥 Best Practices

### 1. Use for streaming data
- APIs
- file chunks
- live feeds

### 2. Combine with async for
```python
async for item in generator():
    await process(item)
```

### 3. Keep it non-blocking
- always use async operations inside

## 📊 Summary
| Concept           | Meaning                             |
|-------------------|-------------------------------------|
| Async generator   | Produces values asynchronously      |
| Keyword           | async def + yield                   |
| Consumption       | async for                           |
| Use case          | Streaming, incremental data         |

## 🔁 Quick Recap
- Async generator yields values over time
- Can use await inside
- Used with async for
- Ideal for streaming and real-time data