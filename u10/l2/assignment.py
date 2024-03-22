def times2(a): return a * 2
def div2(a): return a / 2
def exp2(a): return a ** 2

my_list = [1, 2] 

mapped_times2 = map(times2, my_list)


mapped_times2_list = list(mapped_times2)
print(mapped_times2_list)