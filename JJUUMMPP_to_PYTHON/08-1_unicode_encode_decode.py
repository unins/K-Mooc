import io
import sys
import time
import os

def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


def test1_unicode_utf8_test():
    print(sys.getdefaultencoding())
    print(sys.stdout.encoding)
    print('ㅇㅈㅁㄷㄹㄴㅍㄴㅇㄹㄷㅇㅁㄹ')

for x in range(10):
    print(x, end='')
    sys.stdout.flush()
    time.sleep(1)
