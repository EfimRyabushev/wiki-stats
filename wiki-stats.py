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
                semi_vortexes[i] = final_vortexes[i -1]
            self.edjes = final_links
            self.vertexes = semi_vortexes
            self.names = names
            self.redirects = redirects
            self.sizes = sizes
            self.number_of_redirects =  articles_with_redirection
        print('Граф загружен')

    def check(self):
         print(list(self.vertexes))
         print(list(self.edjes))

    def get_number_of_links_from(self, _id):
        return self.vertexes[_id]

    def get_links_from(self, k):
        return list(self.edjes[self.vertexes[k]:self.vertexes[k+1]])


    def get_id(self, title):
        for i in range(len(self.names)):
            if self.names[i] == title:
               return i

    def get_number_of_articles_with_link(self, number):
        i = 0
        for vertex in self.vertexes:
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

    def number_of_redirects(self):
        return self.number_of_redirects

    def minimal_links(self):
        return  min(self.vertexes[1:])

    def number_of_articles_with_minimal_links(self):
        minimal_links = self.minimal_links()
        counter = 0
        for i in self.vertexes:
            if i == minimal_links:
               counter += 1
        return counter

    def maximal_links(self):
        return  max(self.vertexes[1:])

    def number_of_articles_with_maximal_links(self):
        maximal_links = self.minimal_links()
        counter = 0
        for i in self.vertexes:
            if i == maximal_links:
               counter += 1
        return counter

    def article_with_maximal_links(self):
        maximal_links = self.minimal_links()
        for i in self.vertexes:
            if i == maximal_links:
               return self.get_title(i)


    def mean_number_of_links_in_article(self):
        return statistics.mean([self.number_of_links_to(vertex) for vertex in self.vertexes])

    def links_to_vertex(self, vertex):
         answer = []
         for article in self.vertexes:
             if not self.is_redirect(article) and vertex in self.get_links_from(article):
                answer.append(article)
         return answer

    def number_of_links_to(self, vertex):
        return len(self.links_to_vertex(self, vertex))

    def min_number_of_links_to(self):
        return min([self.number_of_links_to(vertex) for vertex in self.vertexes])

    def number_of_articles_with_min_number_of_links_to(self):
        i = 0
        minimal = self.min_number_of_links_to()
        for vertex in self.vertexes:
            if self.number_of_links_to(vertex) == minimal:
               i += 1
        return i

    def max_links_to_article(self):
        return max([self.number_of_links_to(vertex) for vertex in self.vertexes])

    def number_of_articles_with_max_number_of_links_to(self):
         i = 0
         maximal = self.max_links_to_article()
         for vertex in self.vertexes:
             if self.number_of_links_to(vertex) == maximal:
                i += 1
         return i

    def article_with_max_outer_links(self):
        maximal = self.max_links_to_article()
        for vertex in self.vertexes:
             if self.number_of_links_to(vertex) == maximal:
                return vertex

    def mean_number_of_outer_links(self):
        return statistics.mean([self.number_of_links_to(vertex) for vertex in self.vertexes])

    def redirects_to_article(self, vertex):
         answer = []
         for article in self.vertexes:
            if self.is_redirect(article) and vertex in self.get_links_from(article):
               answer.append(article)
         return answer

    def number_of_redirects_to_article(self, vertex):
        return len(self.redirects_to_article(vertex))

    def max_number_of_redirects(self):
        return max([self.number_of_redirects_to_article(vertex) for vertex in self.vertexes]

    def min_number_of_redirects(self):
        return min([self.number_of_redirects_to_article(vertex) for vertex in self.vertexes]

    def number_of_articles_with_min_number_of_redirects_to(self):
         i = 0
         minimal = self.min_number_of_redirects()
         for vertex in self.vertexes:
             if self.number_of_redirects(vertex) == minimal:
                i += 1
         return i

    def number_of_articles_with_max_number_of_redirects_to(self):
         i = 0
         maximal = self.max_number_of_redirects()
         for vertex in self.vertexes:
             if self.number_of_redirects(vertex) == maximal:
                i += 1
         return i

    def article_with_max_outer_redirects(self):
       maximal = self.max_number_of_redirects()
       for vertex in self.vertexes:
            if self.number_of_links_to(vertex) == maximal:
               return vertex

    def mean_number_of_outer_links(self):
         return statistics.mean([self.number_of_redirects(vertex) for vertex in self.vertexes])

    def number_of_articles_with_number_of_links_to(self, number):
        i = 0
        for vertex in self.vertexes:
            if self.number_of_links_to(vertex) == number:
               i += 1
        return i

    def number_of_articles_with_number_of_redirects(self, number):
        i = 0
        for vertex in self.vertexes:
            if self.number_of_redirects_to_article(vertex) == number:
               i += 1
        return i

def hist(fname, xlabel, ylabel, title, y_objects, x_objects):
    plt.clf()
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.plot(x_objects, y_objects)
    plt.savefiplt.savefig('%s.%s' % (fname, 'png'))

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
wiki = WikiGraph(name)
print('Количество статей с перенаправлением:' + ' ' + str(wiki.number_of_redirects())
print('Минимальное количество ссылок из статьи:' + ' ' + str(wiki.minimal_links()))
print('Kоличество статей с минимальным количеством ссылок:' + ' ' + str(wiki.number_of_articles_with_minimal_links()))
