# generators are used to generate values on the fly
# benefits : save memory, use when require
def generator():
    for i in range(10):
        yield i


gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
