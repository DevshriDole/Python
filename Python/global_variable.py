call_count = 0

def count_function_calls(reset=False):
    global call_count
    if reset:
        call_count = 0
        print("Counter reset.")
    else:
        call_count += 1
        print(f"Function has been called {call_count} times.") 

count_function_calls()

count_function_calls()

count_function_calls(True)

count_function_calls()
