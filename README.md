# Python Scoping & Call Stack Demo

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

A complete demonstration of Python's:
- Variable scoping (LEGB rule)
- Function call stack behavior

## How to Run
```bash
python scoping_and_stacks.py
```

## Code Structure
```python
# Global scope → Enclosing → Local → Built-in
GLOBAL_VAR = "I'm global"

def outer():
    enclosing_var = "I'm enclosing"
    def inner():
        local_var = "I'm local"
        print(GLOBAL_VAR, enclosing_var, local_var)
    inner()
```

## Expected Output
```
=== SCOPING EXAMPLE ===
== Inner Function Accesses ==
I'm local
I'm enclosing
I'm global

=== CALL STACK EXAMPLE ===
Entering level_1
Entering level_2
Entering level_3
...
```

[View full code](scoping_and_stacks.py)
