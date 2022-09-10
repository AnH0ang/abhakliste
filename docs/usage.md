# Usage

## Step 1: Initiate Runner

First you need to initiate the runner by importing the `Abhakliste` class and creating an instance of it.

```python
import subprocess
from abhakliste import Abhakliste

# set up runner
abhaker = Abhakliste()
```

## Step 2: Run Task

There are several ways to run tasks.
The easiest way to run them in context that is initiated by `run_context()`.
The output and error of the code in the context will be collected and displayed later.
In addition there are convinience functions `run_cmd()` and `run_func()` which might also be suitable for your needs.

```python
# run code context
with abhaker.run_context(desc="Run ls"):
  subprocess.check_output("ls")

# run cli command
abhaker.run_cmd("ls", desc="Run ls")

# run function
def run_ls():
  subprocess.check_output("ls")
abhaker.run_func(run_ls, desc="Run ls")
```

## Step 3: Check for failed tasks

At the end of the program, the runner can check and raise an exception if any
of the tasks failed.
This can be used to fail a CI build if any of the tasks failed.

```python
# raise an error if a run failed
abhaker.raise_on_error()
```
