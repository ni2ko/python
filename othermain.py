import dis
def example(x):
     for i in range(x):
         print(2 * i)
dis.dis(example)
