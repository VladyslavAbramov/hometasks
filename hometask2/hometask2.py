import os
import shutil
from datetime import datetime


def time_decor(fn):
    def wrapped(param):
        start = datetime.now()
        fn(param)
        end = datetime.now()
        print(end - start)
        return fn(param)
    return wrapped

@time_decor
def process(string):
    if string[0] != '[' and string[-1] != ']':
        raise ValueError('Not list')
    try:
        arr = list(map(lambda x: int(x), string[1:-1].split(',')))
    except BaseException:
        raise ValueError('Not integer')
    return sum(arr)


def monitor(read_catalog=r'D:\ITEA\lesson2\test\input',
            write_catalog=r'D:\ITEA\lesson2\test\output',
            error_catalog=r'D:\ITEA\lesson2\test\error'):
    files = os.listdir(read_catalog)
    list_txt = list(filter(lambda x: x[-3:] == 'txt', files))

    if len(list_txt) > 0:
        for file_txt in list_txt:
            try:
                with open(read_catalog + '\\' + file_txt, 'r', encoding='utf-8') as f,\
                        open(write_catalog + '\\' + file_txt, 'w') as w:
                    w.write(str(process(f.read())))
                os.remove(read_catalog + '\\' + file_txt)
            except BaseException:
                shutil.copy(read_catalog + '\\' + file_txt, error_catalog)
                os.remove(write_catalog + '\\' + file_txt)

