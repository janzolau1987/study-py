#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os, time, random
from multiprocessing import Process, Pool
import subprocess

# 多进程

# python的os模块封装了常见的系统调用，其中就包括fork()，可以在python程序中轻松创建子进程
print('Process (%s) start...' % os.getpid())


# Only work on Unix/Linux/Mac
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


# if __name__ == '__main__':
#    print('Parent process %s.' % os.getpid())
#    p = Process(target=run_proc, args=('test',))
#    print('Child process will start.')
#    p.start()   # 启动子进程
#    p.join()    # 等待子进程结束后再继续往下运行
#    print('Child process end.')

# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds' % (name, (end - start)))

# if __name__=='__main__':
#    print('Parent process %s.' % os.getpid())
#    p = Pool(4)
#    for i in range(5):
#        p.apply_async(long_time_task, args=(i,))
#    print('Waiting for all subprocess done...')
#    p.close()
#    p.join()    # 等待所有子进程执行完毕
#    print('All subprocess done.')

# 控制子进程的输入和输出
print('$nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

# 如果子进程需要输入，则可以通过communicate()方法输入
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)


