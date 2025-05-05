"""
PYTHON SCOPING & CALL STACK DEMONSTRATION
-----------------------------------------
This file combines all concepts into one executable example.
Run with: `python scoping_and_stacks.py`
"""

# ====================
# SECTION 1: SCOPING
# ====================
print("\n=== SCOPING EXAMPLE ===\n")

# Global scope
GLOBAL_VAR = "I'm global (module-level)"

def outer_function():
    """Enclosing scope demonstration"""
    enclosing_var = "I'm in enclosing scope (outer_function)"
    
    def inner_function():
        """Local scope demonstration"""
        local_var = "I'm in local scope (inner_function)"
        print("== Inner Function Accesses ==")
        print(local_var)      # Local
        print(enclosing_var)  # Enclosing
        print(GLOBAL_VAR)     # Global
        print(len([1,2,3]))  # Built-in (len)
    
    inner_function()
    
    print("\n== Outer Function Accesses ==")
    print(enclosing_var)
    print(GLOBAL_VAR)
    # print(local_var)  # Would raise NameError (out of scope)

outer_function()

print("\n== Global Accesses ==")
print(GLOBAL_VAR)
# print(enclosing_var)  # Would raise NameError (out of scope)

# ====================
# SECTION 2: CALL STACK
# ====================
print("\n=== CALL STACK EXAMPLE ===\n")

def level_1():
    print("Entering level_1")
    level_2()
    print("Exiting level_1")

def level_2():
    print("Entering level_2")
    level_3()
    print("Exiting level_2")

def level_3():
    print("Entering level_3")
    print("Stack depth example (innermost level)")
    print("Exiting level_3")

level_1()  # Triggers the call stack sequence

# ====================
# SECTION 3: COMBINED DEMO
# ====================
print("\n=== COMBINED SCOPING + STACK DEMO ===\n")

def parent_function():
    parent_var = "Parent scope"
    
    def child_function():
        child_var = "Child scope"
        print(f"Child accesses: {parent_var} AND {child_var}")
    
    child_function()
    # print(child_var)  # Would error - child_var not accessible here

parent_function()

# ====================
# EXECUTION CONTROLS
# ====================
if __name__ == "__main__":
    print("\n=== PROGRAM EXECUTION COMPLETE ===")