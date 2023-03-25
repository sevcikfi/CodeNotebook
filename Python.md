---
alias:
tag: IT/languages CodeNotebook 
---

# Python

## Install

### Virtual env

FIX: use Anaconda or virtualenv with requirements.txt

```bash
#create env
python -m venv /path/to/new/virtual/environment
#active the env
source env/bin/activate
#deactivate
deactivate
#export package list
python -m pip freeze > requirement.txt
#install from list
python -m pip install -r /path/to/requirements.txt
```

### Jupyter notebooks

Linux needs `python3-dev` package and then run `pip install jupyter` and wait for 10mins, then run:

```bash
# Replace <PORT> with your selected port number
jupyter notebook --no-browser --port=<PORT>
# Replace <PORT> with the port number you selected in the above step
# Replace <REMOTE_USER> with the remote server username
# Replace <REMOTE_HOST> with your remote server address
ssh -L <LOCAL-PORT>:localhost:<REMOTE-PORT> <REMOTE_USER>@<REMOTE_HOST>
```

## Basics

### print formatter

[see pyformat website](https://pyformat.info)

### Common mistakes

1. Use `f"{string}"` instead of `+`
2. Use `with` instead of manually closing IO streams, with context managers (networking, pools)
3. Bare `except:` (catching CTRL-C) instead of `except <Exception>:`
4. `^` instead of `**`
5. Empty mutable argument defaults instead of `None`
6. Not using comprehensions (excessive for-loops), list[], dict{:}, set{}, generator()
7. Unreadable flexing 10X dev code
8. Equality checking #1: `==` for `isInstance()` (type checking)
9. Equality checking #2: `==` for `is` identity
10. Equality checking #3: `!= 0` for `bool()` built-in
11. Doing stuff manually instead of using libraries such as *numpy, matplotlib, Pandas, Scipy, PyTorch, numba...*
12. Loop #0: Manual for-loops instead of built-in or library function (*numpy* for arrays etc)
13. Loop #1: `range(len(a))` instead *for each*
14. Loop #2: `enumerate(a)` to get both index and element
15. Loop #3: `zip(a,b)` for two objects, `enumerate(zip(a,b))` if index required
16. Loop #4: `for k in d.key()` instead of just `for k in d`
17. Loop #5: `for k, v in d.item()` instead of doing so manually
18. Tuple unpacking: `x, y = point` instead of using indexes
19. `time.time()` instead of `time.perf_counter()`
20. *prints* instead of *logging* module
21. `shell=True` on *subprocess* module
22. PEP8 exists for reason xd

### Logging

Most basic logging can be done with native *logging* module:

```Python
import logging
level = logging.DEBUG #lowest logging level
format = '[%(level_name)s] %(asctime)s - %(message)s' #message format
logging.debug("debug message") #debug/info/error
logging.basicConfig(level=level, format=format)
#prints [DEBUG] 2022-08-23 2:15:22 - debug message
```

## Advanced

### CPU isn't alone

*We have walked through the most popular forms of concurrency. But the question remains - when should choose which one? It really depends on the use cases. From my experience (and reading), I tend to follow this pseudo code:*

```Python
if io_bound:
    if io_very_slow:
        print("Use Asyncio")
    else:
        print("Use Threads")
else:
    print("Multi Processing")
```

For summary, see [Thread #0] bellow or read the write-up in [ComSci](ComputerScience.md).
In short, async/await for slower IO, Thread(PoolExecutor) for faster IO, multiprocessing to kill the GIL and use all CPUs.

## Sources

[Threads #0](https://leimao.github.io/blog/Python-Concurrency-High-Level/)
