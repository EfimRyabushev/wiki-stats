
import os
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)




class WikiGraph():
    def __init__(self, name):
        self.load_from_file(name)
    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            number_of_article, number_of_links = f.readline().split()
            number_of_article, number_of_links = int(number_of_article), int(number_of_links)
            counter = 0
            number_of_link = 0
            names = []
            sizes = []
            redirects = []
            articles_with_redirection = 0
            final_vortexes = array.array('I', [1]*number_of_article)
            final_links = array.array('I', [1]*number_of_links)
            while counter <= number_of_article - 1:
                  name = f.readline().rstrip()
                  size, flag, links = f.readline().rstrip().split()
                  links, flag = int(links), int(flag)
                  names.append(name)
                  sizes.append(int(size))
                  if flag == 1:
                     articles_with_redirection += 1
                     redirects.append(True)
                  else:
                     redirects.append(False)
                  final_vortexes[counter] = links
                  for i in range(links):
                      target_link = int(f.readline().rstrip())
                      final_links[number_of_link] = target_link
                      number_of_link += 1
                  counter += 1

            self.articles_with_redirection = articles_with_redirection
            semi_vortexes = array.array('I', [0]*(number_of_article + 1))
            for i in range(1, number_of_article):
                semi_vortexes[i] = sum(final_vortexes[0:i -1])
            self.edjes = final_links
            self.vertexes = semi_vortexes
            self.names = names
            self.redirects = redirects
            self.sizes = sizes
            self.number_of_redirects =  articles_with_redirection
        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return len(self.get_links_from(_id))

    def get_links_from(self, k):
           if k  != len(self.vertexes) - 1:
              return list(self.edjes[self.vertexes[k]:self.vertexes[k + 1]])
           else:
               return list(self.edjes[self.vertexes[k]:])



    def get_id(self, title):
        for i in range(len(self.names)):
            if self.names[i] == title:
               return i + 1

    def get_number_of_articles_with_link(self, number):
        i = 0
        for vertex in range(len(self.vertexes) - 1):
            if self.get_number_of_links_from(vertex) == number:
               i += 1
        return i

    def get_number_of_pages(self):
        return len(self.names)

    def is_redirect(self, _id):
        return self.redirects[_id]

    def get_title(self, _id):
        return self.names[_id]

    def get_page_size(self, _id):
        return self.sizes[_id]

    def number_of_redirects_from(self):
        return self.number_of_redirects

    def minimal_links(self):
        return  min(self.vertexes[1:])

    def number_of_articles_with_minimal_links(self):
        minimal_links = self.minimal_links()
        return self.get_number_of_articles_with_link(minimal_links)

    def maximal_links(self):
        return  max([self.get_number_of_links_from(i) for i in range(len(self.vertexes) - 1)])

    def number_of_articles_with_maximal_links(self):
        maximal_links = self.maximal_links()
        return self.get_number_of_articles_with_link(maximal_links)

    def article_with_maximal_links(self):
        maximal_links = self.maximal_links()
        for i in range(len(self.vertexes) - 1):
            if self.get_number_of_links_from(i) == maximal_links:
               return self.get_title(i - 1)

    def mean_number_of_links_in_article(self):
        return statistics.mean([self.get_number_of_links_from(vertex) for vertex in range(len(self.vertexes) - 1)])

    def links_to_article(self, vertex):
        answer = []
        for node in range(len(self.vertexes) - 1):
            if vertex in self.get_links_from(node):
                answer.append(node)
        return answer

    def number_of_links_to(self, vertex):
        return len(self.links_to_article(vertex))

    def min_number_of_outer_links(self):
        return min([self.number_of_links_to(vertex) for vertex in range(len(self.vertexes) - 1)])

    def max_number_of_outer_links(self):
        return max([self.number_of_links_to(vertex) for vertex in range(len(self.vertexes) - 1)])

    def number_of_articles_with_min_number_of_outer_links(self):
        minimal = self.min_number_of_outer_links()
        counter = 0
        for vertex in range(len(self.vertexes) - 1):
            if self.number_of_links_to(vertex) == minimal:
                counter += 1
        return counter

    def number_of_articles_with_max_number_of_outer_links(self):
        maximal = self.max_number_of_outer_links()
        counter = 0
        for vertex in range(len(self.vertexes) - 1):
            if self.number_of_links_to(vertex) == maximal:
                counter += 1
        return counter

    def article_with_min_number_of_outer_links(self):
        maximal = self.max_number_of_outer_links()
        for vertex in range(len(self.vertexes) - 1):
            if self.number_of_links_to(vertex) == maximal:
                return self.get_id(vertex)


def hist(fname, xlabel, ylabel, title, y_objects, x_objects):
    plt.clf()
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.plot(x_objects, y_objects)
   # plt.savefiplt.savefig('%s.%s' % (fname, 'png'))

def first_hist(wiki):
    x_objects = range(wiki.maximal_links())
    y_objects = [wiki.get_number_of_articles_with_link(i) for i in x_objects]
    hist('first_hist', 'number_of_links', 'number_of_articles', y_objects, x_objects)

def second_hist(wiki):
    x_objects = range(wiki.max_links_to_article())
    y_objects = [wiki.number_of_articles_with_number_of_links_to(i) for i in x_objects]
    hist('second_hist', 'number_of_links_to', 'number_of_articles', y_objects, x_objects)

def third_hist(wiki):
    x_objects = range(wiki.max_links_to_article())
    y_objects = [wiki.number_of_articles_with_number_of_redirects(i) for i in x_objects]
    hist('second_hist', 'number_of_links_to', 'number_of_articles', y_objects, x_objects)

name = '/home/student/a/wiki_small.txt'
wiki = WikiGraph(name)
index = wiki.get_id('Python')
#Загружаю граф из файла: wiki_small.txt
#Граф загружен
#Количество статей с перенаправлением: 50 (4.13%)
#Минимальное количество ссылок из статьи: 0
#Количество статей с минимальным количеством ссылок: 3
#Максимальное количество ссылок из статьи: 356
#Количество статей с максимальным количеством ссылок: 1
#Статья с наибольшим количеством ссылок: Python
#Среднее количество ссылок в статье: 34.34 (ср. откл. 32.55)
#Минимальное количество ссылок на статью: 0
#Количество статей с минимальным количеством внешних ссылок: 146
#Максимальное количество ссылок на статью: 1000
#Количество статей с максимальным количеством внешних ссылок: 1
#Статья с наибольшим количеством внешних ссылок: Python
#Среднее количество внешних ссылок на статью: 32.52 (ср. откл. 68.19)
#Минимальное количество перенаправлений на статью: 0
#Количество статей с минимальным количеством внешних перенаправлений: 1171
#Максимальное количество перенаправлений на статью: 7
#Количество статей с максимальным количеством внешних перенаправлений: 1
#Статья с наибольшим количеством внешних перенаправлений: Python
#Среднее количество внешних перенаправлений на статью: 0.04 (ср. откл. 0.28)
#Запускаем поиск в ширину
#Поиск закончен. Найден путь:
#Python
#UNIX
#Список_файловых_систем
#print(wiki.get_id(wiki.vertexes[1]))
print('Минимальное количество ссылок из статьи:' + ' ' + str(wiki.minimal_links()))
print('Kоличество статей с минимальным количеством ссылок:' + ' ' + str(wiki.number_of_articles_with_minimal_links()))
print('Максимальное количество ссылок из статьи:' + ' ' + str(wiki.maximal_links()))
print('Количество статей с максимальным количеством ссылок:' + ' ' + str(wiki.number_of_articles_with_maximal_links()))
print('Статья с наибольшим количеством ссылок:' + ' ' + str(wiki.article_with_maximal_links()))
print('Среднее количество ссылок в статье:' + ' ' + str(wiki.mean_number_of_links_in_article()))
print('Минимальное количество ссылок на статью:' + ' ' + str(wiki.min_number_of_outer_links()))
print('Количество статей с минимальным количеством внешних ссылок: ' + str(wiki.number_of_articles_with_min_number_of_outer_links()))
print('Максимальное количество ссылок на статью: ' + str(wiki.max_number_of_outer_links()))
print('Количество статей с максимальным количеством внешних ссылок: ' + str(wiki.number_of_articles_with_max_number_of_outer_links()))
print('Статья с наибольшим количеством внешних ссылок: ' + str(wiki.article_with_min_number_of_outer_links()))
'''print('Среднее количество внешних ссылок на статью: ' + str(wiki.mean_number_of_outer_links()))
print('Количество статей с минимальным количеством внешних перенаправлений: ' + str(wiki.number_of_articles_with_min_number_of_redirects_to()))
print('Максимальное количество перенаправлений на статью: ' + str(wiki.max_number_of_redirects()))
print('Количество статей с максимальным количеством внешних перенаправлений: ' + str(wiki.number_of_articles_with_max_number_of_redirects_to()))
print('Статья с наибольшим количеством внешних перенаправлений: ' + str(wiki.article_with_max_outer_redirects()))
print('Среднее количество внешних перенаправлений на статью: ' + str(wiki.mean_number_of_redirects()))'''
