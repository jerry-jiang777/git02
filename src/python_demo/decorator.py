def outer(origin_func):
    def inner(*args, **kwargs):
        print(f'装饰器开始执行...')
        res = origin_func(*args, **kwargs)
        print(f"装饰器调用结束...")
        return res
    return inner

@outer
def add(x, y):
    return x + y


print(add(2, 3))