import redis
import os
from multiprocessing import Process, Queue ,Pool

amount_process = 3


q=Queue()
workers = []
r = redis.StrictRedis(host='localhost', port=6379, db=0)
rootdir = '/home/user/TextData/Breach/data'

def walker(q):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            print(os.path.join(subdir, file))
            q.put(os.path.join(subdir, file))


def worker(q):
    while True:
        file = q.get()
        with open(file, "r", encoding="ISO-8859-1") as f:
            for i in f:
                try:
                    for line in f:
                        email = line.split(":")[0]
                        domain = email.split("@")[1].lower()
                        password = line.split(":")[1]
                        query = "{email:" + email + ", password:" + password[:-1] + "}"
                        r.sadd(domain, query)
                except:
                    pass
        if file is -1:
            break




print("start")
walker_proc = Process(target=walker,args=(q,))


for i in range(amount_process):
    workers.append(Process(target=worker, args=(q,)))




walker_proc.start()

for i in workers:
    i.start()
q.close()
q.join_thread()

walker_proc.join()
for i in workers:
    i.join()