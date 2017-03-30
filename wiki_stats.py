#!/usr/bin/python3

import os
import sys
import math

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)
        kadyrov = 0
        with open(filename) as f:
            n, _nlinks = [int(j) for j in f.readline().split()]  
            self._titles = []
            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n+1))
            i = 1
            for i in range(n):
                self._titles.append(f.readline())
                self._sizes[i], self._redirect[i], number_of_links = [int(j) for j in f.readline().split()]
                for j in range(number_of_links):
                    self._links[kadyrov+j] = int(f.readline())
                kadyrov += number_of_links
                self._offset[i+1] = kadyrov
      
        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return self._offset[_id+1] - self._offset[_id]

    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id+1]]

    def get_id(self, title):
        return self._titles.index(title)

    def get_number_of_pages(self):
        return len(self._titles)

    def is_redirect(self, _id):
        return self._redirect[_id]

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл



if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)

print(sum(wg._redirect))
_min = float('INF')
min_number = 0
_max = -1
max_number = 0
ID_max = -1
for i in range(1, wg.get_number_of_pages()):
    if wg.get_number_of_links_from(i) < _min:
        _min = wg.get_number_of_links_from(i)
        min_number = 1
    elif wg.get_number_of_links_from(i) == _min:
        min_number += 1
    if wg.get_number_of_links_from(i) > _max:
        _max = wg.get_number_of_links_from(i)
        max_number = 1
        ID_max = i
    elif wg.get_number_of_links_from(i) == _max:
        max_number += 1
print(_min)
print(min_number)
print(_max)
print(max_number)
print(wg.get_title(ID_max))

massive = [0]*wg.get_number_of_pages()
for i in range(wg.get_number_of_pages()):
    for page in wg.get_links_from(i):
        massive[page] += 1
print(min(massive))
print(massive.count(min(massive)))
print(max(massive))
print(massive.count(max(massive)))
print(wg.get_title(massive.index(max(massive))))









# TODO: статистика и гистограммы
