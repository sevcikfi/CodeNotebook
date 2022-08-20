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

## Basics

### print formater

[see pyformat website](https://pyformat.info)

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
In short, async/awant for slower IO, Thread(PoolExecutor) for faster IO, multiprocessing to kill the GIL and use all CPUs.

## Sources

[Threads #0](https://leimao.github.io/blog/Python-Concurrency-High-Level/)
