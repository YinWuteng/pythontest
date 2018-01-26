# -*- coding:utf-8 -*-
# print('hi', "hao", "a")
# print('I\'m ok.')
# print(ord('A'))
# string = 'hello %s' % 'world'
# print(string)
# str = 'hi %s,you have a %d' % ('tina', 1000)
# print(str)
# s1=72
# s2=85
# r=(72-85)/72
# print(r)
# classmates = ['bob', 'mary', 'fake']
# # print(classmates[-1])
# classmates.insert(1, 'ben')
# print(classmates)
# classmates.append('wolf')
# print(classmates)
# classmates[2] = 'wolf'
# print(classmates)
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0])
# print(L[1][0])
# print(L[2][-1])
# L = []
# n = 1
# S = []
# while n <= 99:
#     L.append(n)
#     n += 2
# print(L)
# for i in L:
#     if i <= L.__len__():
#         print(L[i])
# list = list(range(1, 20, 3))
# print(list)
# import os
#
# print('Process (%s) start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
# from multiprocessing import Pool
# import os, time, random
#
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getppid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds' % (name, end - start))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')
# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)
# from multiprocessing import Process, Queue
# import os, time, random
#
#
# # 写数据进程执行的代码
# def write(q):
#     print('Process to write %s.' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
#
# # 读取数据执行的代码
# def read(q):
#     print('Process to read %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
#
# if __name__ == '__main__':
#     # 父进程创建Quene
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     #启动子进程pw，写入：
#     pw.start()
#     # 启动子进程pr，读取
#     pr.start()
#     # 等待pw结束
#     pw.join()
#     # pr进程是死循环，无法等待其结束，只能强行终止
#     pr.terminate()
# import time, threading
#
#
# # 新线程执行的代码
# def loop():
#     print('threading %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop(), name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)
# import threading, time
#
# # 银行存款
# balance = 0
# lock = threading.Lock()
#
#
# def change_it(n):
#     # 先存后取，结果应该为0
#     global balance
#     balance = balance + n
#
#
# def run_thread(n):
#     for i in range(1000000):
#         # 先要获取锁
#         lock.acquire()
#         try:
#             # 修改余额
#             change_it(n)
#         finally:
#             # 释放锁
#             lock.release()
#
#
# t1 = threading.Thread(target=run_thread, args=(8,))
# t2 = threading.Thread(target=run_thread, args=(-6,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# import threading
#
# # 创建全局ThreadLocal对象
# local_school = threading.local()
#
#
# def process_student():
#     std = local_school.student
#     print('Hello,%s (in %s)' % (std, threading.current_thread().name))
#
#
# def process_thread(name):
#     # 绑定ThreadLocal的Student
#     local_school.student = name
#     process_student()
#
#
# t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()
import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接受结果的队列
result_queue = queue.Queue()


# 从BaseManbger继承QueueManger
class QueueManger(BaseManager):
    pass


# 把两个Queue都注册到网络上，callable参数关联了Queue对象
QueueManger.register('get_task_queue', callable=lambda: task_queue)
QueueManger.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口500，设置验证码'abc'
manger = QueueManger(address=('', 5000), authkey=b'abc')
# 启动Queue
manger.start()
# 通过网络访问Queue对象
task = manger.get_task_queue()
result = manger.get_result_queue()
# 放几个任务进去
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d' %n)
    task.put(n)
# 从result队列读取结果
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result:%s' % r)
# 关闭
manger.shutdown()
print('master exit.')
