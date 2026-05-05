# How to Identify Blocking Operations?

## ❓ Basic Question
**How can we tell if a piece of code is blocking and will break async behavior?**

---

## 🧠 Short Answer

👉 If an operation:
- **does not use `await`**
- **holds execution until it finishes**

👉 It is likely **blocking**

---

## ⚙️ Quick Identification Rules


### 1. ❌ No `await` in async code

If you see:

```python
def some_function():
    ...

or inside async:

result = some_sync_call()
```

👉 Suspicious → could be blocking

### 2. 📚 Library Type Check

Ask:

>“Is this library async-aware?”

- Uses async/await → ✅ non-blocking
- Normal sync API → ❌ blocking

### 3. ⏳ It “waits” visibly

Operations that:

- take time
- pause execution
- return only after completion

👉 Usually blocking

### 4. 🔍 Known Blocking Patterns

Common red flags:

- `time.sleep()`
- synchronous HTTP calls
- file read/write (normal open)
- database calls without async driver
- heavy computation

### 5. 🧪 Behavior Test (Mental)

Ask:

> "If this runs, can other async tasks continue?"
 - Yes → non-blocking
 - No → blocking

## 🏠 Real-Life Analogy

### 🚦 Traffic Signal
 - Blocking → road closed 🚫 (everything stops)
 - Async → lane switch 🔄 (others keep moving)

## 🧠 Mental Model
- Blocking = holds control
- Async = releases control

## ⚠️ Subtle Case (Important)

Some functions look safe but are blocking:

- CPU-heavy loops
- large data processing
- synchronous wrappers inside async code

👉 Even without sleep, they can still block

## 📊 Quick Checklist
| Question                     | If YES → Blocking? |
|------------------------------|--------------------|
| No await used?               | Likely             |
| Uses sync library?           | Likely             |
| Takes time to finish?        | Likely             |
| Prevents other tasks?        | Definitely         |

## 🔥 Key Takeaway

- 👉 Blocking operations are those that do not give control back to the event loop.
- 👉 Always verify whether your code or library is async-compatible.