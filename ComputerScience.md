# ComSci

file discussing ComSci paradigmas and other advanced topics possible mentioned in lang specific mds in their respective folders

## Advanced stuff

### How to deal with more cores

**Paralelism**: CPU Bound => Multi Processing

- you're running stuff in pararel and taking advante of multiple CPUs

**Concurency**: I/O Bound, Fast I/O, Limited Number of Connections => Multi Threading

- concurently running more tasks on one thread, context switching

**Ansynchro**: I/O Bound, Slow I/O, Many connections => Asyncio

- using async/awats, waiting thread can let futher code continue executing and the results from awaiting one are either received or needed
 
NOTE: low level languages such as C/C++, C#, Java achieve native paralelism computing by using threads, higher ones such as *SnekTM*🐍 and Google's abonimation of Go locks down interpreters (GIL) and forces you to use futher libraries (Multiprocessing) or tidious workarounds ((G|c)orutines)

## Sources

[Threads #0](https://leimao.github.io/blog/Python-Concurrency-High-Level/) - summarizes the latter two
[Threads #1](http://masnun.rocks/2016/10/06/async-python-the-different-forms-of-concurrency/)
[Threads #2](https://realpython.com/python-concurrency/) - long article with examples specific for Python
