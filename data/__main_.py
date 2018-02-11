import sys

from data.db.mongodb import write_mongodb
from data.random.generator import data_generate


def writer():
    print("====== generate start ======")
    loop_start = 1
    loop_end = 1000001
    batch_size = 100
    loop_total = loop_end - loop_start
    base_num = loop_total / batch_size
    for j in range(loop_start, loop_end):
        json = []
        for i in range(batch_size):
            json.append(data_generate())
        write_mongodb(json)
        sys.stdout.write("\r")
        sys.stdout.write("%s%% |%s| %s/%s" % (int(j / base_num % 101), int(j / base_num % 101) * '#', loop_total * batch_size, j * batch_size))
        sys.stdout.flush()
    print("\n====== generate end ======")


if __name__ == "__main__":
    writer()