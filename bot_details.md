# Code explanations and other notes and info


### The order of execution for the code in bait_scammer.py:

1. First, the imports at the top of the file are processed. This includes standard library imports, third-party imports (like Selenium), and local imports (config, constants, utils).

2. The `ScamBaitBot` class is defined, but no code within it is executed yet.

3. After the class definition, we reach the executable code at the bottom of the file:

   ```python
   bot = ScamBaitBot()
   ```
   This line creates an instance of the `ScamBaitBot` class. When this happens:
   - The `__init__` method is called, which sets `self.start_time` to the current time.

4. ```python
   print(bot)
   ```
   This line prints the bot instance. It implicitly calls the `__repr__` method, which returns a string representation of the bot, including its runtime (which will be very close to 0 at this point).

5. ```python
   bot.run_bot()
   ```
   This line calls the `run_bot` method of the bot instance. This method, in turn, calls:
   - `self.func_one()` (which prints "Function 1")
   - `self.func_two()` (which prints "Function 2")
   - `self.func_three()` (which prints "Function 3")

6. ```python
   print(bot)
   ```
   This final line prints the bot instance again. The `__repr__` method is called again, but this time the runtime will be longer, reflecting the time taken to execute the `run_bot` method.

So, in summary, the order of visible output would be:
1. The result of the first `print(bot)` (showing a runtime close to 0)
2. "Function 1"
3. "Function 2"
4. "Function 3"
5. The result of the second `print(bot)` (showing a longer runtime)

This execution order allows you to see the initial state of the bot, watch it perform its functions, and then see its final state, which includes how long it took to run.0k

<br>

## Order of code execution

1. The class is defined: `ScamBaitBot:`
2. Then the executable code: `bot = ScamBaitBot()` is reached
3. That creates an instance of the `ScamBaitBot`
4. Which calls the `__init__()` method.
5. The `__init__()` call sets `self.start_time` to the current time.
6. `print(bot)` prints the instance and implicitly calls the `__repr__()` method, which returns a string representation of the bot.
7. Then `bot.run_bot()` calls the `run_bot()` method. (Note: It's `run_bot()`, not `run_run_bot()`)
8. Calling the `run_bot()` method then calls the individual `self.func_one()`, `self.func_two()`, and `self.func_three()` methods in that order.
9. The final line `print(bot)` prints the bot instance again,
10. which calls the `__repr__()` method again

<br>

**bait_scammer.py**
```python
# Order of code execution
# ------------------------------------
# 1. The class is defined: `ScamBaitBot:`
# 2. Then the executable code: `bot = ScamBaitBot()` is reached
# 3. That creates an instance of the `ScamBaitBot`
# 4. Which calls the `__init__()` method.
# 5. The `__init__()` call sets `self.start_time` to the current time.
# 6. `print(bot)` prints the instance and implicitly calls the `__repr__()` method, which returns a string representation of the bot.
# 7. Then `bot.run_bot()` calls the `run_bot()` method. (Note: It's `run_bot()`, not `run_run_bot()`)
# 8. Calling the `run_bot()` method then calls the individual `self.func_one()`, `self.func_two()`, and `self.func_three()` methods in that order.
# 9. The final line `print(bot)` prints the bot instance again,
# 10. which calls the `__repr__()` method again

class ScamBaitBot:
    """1. STEP ONE: define the class
       3. bot = ScamBaitBot() creates an instance of the ScamBaitBot class
       4. which calls the __init__ method.
    """
    
    def __init__(self):
        """5. the init sets self.start_time with the current time"""   
        self.start_time = time.time()

    # 6b.repr is implicitly called by print(bot)
    def __repr__(self):
        return f"ScamBaitBot(runtime={time.time() - self.start_time:.2f}s)"

    def func_one(self):
        print("Function 1")

    def func_two(self):
        print("Function 2")

    def func_three(self):
        print("Function 3")

    # 7b.  run_bot method is called by: bot.run_bot()
    def run_bot(self):
        # 8. The methods are called sequentially.
        self.func_one()
        self.func_two()
        self.func_three()


# 2. After the class is defined, 
# The executable code at the bottom of the file is reached:
# Which creates an instance of the `ScamBaitBot` step 3. (see the class definition above)
bot = ScamBaitBot()

# 6a. print(bot) prints the bot instance and, Implicitly calls the __repr__ method, and
print(bot)  
# returns a string representation of the bot instance
# and will print something like: ScamBaitBot(runtime=0.00s)

# 7a. calls the:  def run_bot(self)  method of the bot instance
bot.run_bot() 

# 9. The final print(bot) line prints the bot instance again.
# 10. And, calls the  __repr__ method again
print(bot)  # This will print something like: ScamBaitBot(runtime=1.23s)
```

# Output:
```bash
ScamBaitBot(runtime=0.00s)
Function 1
Function 2
Function 3
ScamBaitBot(runtime=0.00s)
```
