import multiprocessing
import time

start = time.perf_counter()


def do_something():
    print("Sleeping for 1 second")
    time.sleep(1)
    print("Done Sleeping...")


# do_something()
# do_something()
#
# finish = time.perf_counter()
# print(f"Finished in {round(finish - start, 2)} second(s)")

# in the prev use case do something executes sequentially

"""
To make use of multi processing in the above use case
"""

process_1 = multiprocessing.Process(target=do_something)
process_2 = multiprocessing.Process(target=do_something)

process_1.start()
process_2.start()

process_1.join()
process_2.join()

finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} second(s)")
