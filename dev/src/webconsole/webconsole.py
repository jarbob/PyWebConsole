# coding: UTF-8

import Queue
import subprocess
import threading
import time


# event = threading.Event()

output_queue = Queue.Queue(maxsize=0)
input_queue = Queue.Queue(maxsize=0)

handle = []


# 单例模式,防止多次实例化
class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
            return cls.instance


class CommandHandle(object):
    __metaclass__ = Singleton
    global input_queue

    def __init__(self):
        self.__command = None
        self.__handle()

    def __handle(self):
        while True:

            if input_queue.qsize() > 0:
                self.__command = input_queue.get()
                print self.__command
                if str(self.__command).find('stop') != -1:
                    # todo-me stop command
                    # if event.isSet():
                    #     event.clear()
                    threading.Thread(target=stop).start()

                    print '---------stop------------'
                else:

                    threading.Thread(target=run, args=(self.__command,)).start()
                    # event.set()
            time.sleep(1)


def run(arg):
    stop()
    global handle
    handle.append(Console(arg))
    for h in handle:
        h.execute()


def stop():
    global handle
    if len(handle):

        try:
            for h in handle:
                h.kill()

        except Exception, e:
            # print Exception, e
            output_queue.put(e)
        handle = []


class Console:
    global output_queue

    def __init__(self, arg):
        self.__arg = arg
        self.__total = 1
        self.__obj = None
        # self.__queue = my_queue

    def execute(self):
        # print self.__arg
        try:
            obj = subprocess.Popen(self.__arg, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            # event.wait()
        except Exception, e:
            print e
            output_queue.put(e)
        else:
            self.__obj = obj
            data = obj.poll()
            while data is None:
                line = obj.stdout.readline()
                data = obj.poll()
                line = line.strip()
                print 'line ', self.__total, line
                output_queue.put(line)
                self.__total += 1
                # event.set()
        finally:
            output_queue.put(0)

    def kill(self):
        if self.__obj:
            self.__obj.kill()
            output_queue.put('-' * 30 + 'stop' + '-' * 30)


def test(arg):
    Console(arg).execute()


def get_data():
    while True:
        if output_queue.qsize() > 0:
            return output_queue.get()
        else:
            return 0


if __name__ == '__main__':
    test('ping -c12 jarbob.com')
    t = threading.Thread(target=test, args=('ping -c12 jarbob.com',))
    t.setDaemon(True)

    t.join()

    t1 = threading.Thread(target=get_data)
    t1.start()
    t.start()
