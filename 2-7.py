# -*- coding: UTF-8 -*-

# 如何实现用户的历史记录功能(最多n条)

from random import randint
from collections import deque

history = deque([], 5)
N = randint(0, 100)

"""
import pickle
# 保存
pickle.dump(history, open( 'history.txt', 'w', encoding='utf-8'))
# 读取
pickle.load(open('history.txt', 'r', encoding='utf-8'))

"""


def guess(guess_num):
    if guess_num == N:
        print('right')
        return True
    elif guess_num < N:
        print('You need guess lager number: ')
        return False
    else:
        print('You need guess smaller number: ')
        return False


while True:
    guess_num = input('请才一个数字并输入:')
    if guess_num.isdigit():
        k = int(guess_num)
        history.append(k)
        if guess(k):
            break
    elif guess_num == 'history' or guess_num == 'h?':
        print(list(history))



