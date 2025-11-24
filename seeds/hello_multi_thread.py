from concurrent.futures import ThreadPoolExecutor, as_completed

def test(str):
    print("Hello\n")

p_cnt = 3
pool_list = []
thread_pool = ThreadPoolExecutor(p_cnt)
str = ''
for index in range(0,3):
    pool_list.append(thread_pool.submit(test, str,))
for fu in as_completed(pool_list):
    res = fu.result()