# python 装饰器
##### 目的：　不改变对象的业务逻辑的基础上增添新的功能
##### 原理：　万物皆是对象
##### 作用：　面向切面编程

### 举例-log
```python
def log(func):
    def wrapper():
        print('%s is running' % func.__name__)
        return func()
    return wrapper

def f1():
    print('f1 here')

f1 = log(f1)
f1()

# 输出：
#f1 is running
#f1 here
```
使用@
```python
def log(func):
    def wrapper():
        print('%s is running' % func.__name__)
        return func()
    return wrapper

@log
def f1():
    print('f1 here')

f1()
# 输出：
#f1 is running
#f1 here
```

问题与优化 
此时打印f1函数的__name__发现是wrapper,因为函数复制了名字和解释等, 可以采用functools

```python
import functools
def log(func):
    functools.wrap('func')
    def wrapper():
        print('%s is running' % func.__name__)
        return func()
    return wrapper

@log
def f1():
    print('f1 here')

f1()
# 输出：
#f1 is running
#f1 here
```

### 应用-限制函数的运行时间
```python
import signal
import time
def set_timeout(num, callback):
    def decorator(func):
        def myHander(signum, frame):
            raise Exception('jankin error')

        def wrapper():
            try:
                signal.signal(signal.SIGALRM, myHander) # 注册信号监听
                signal.alarm(num) #　定时执行
                r = func()
                signal.alarm(0) # 关闭定时执行
                return r
            except Exception as e:
                print('time out')
                callback()
        return wrapper
    return decorator


def timeout():
    print('time out 111')


@set_timeout(2, timeout)
def foo():
    time.sleep(3)
    print("i am foo")

foo()
```