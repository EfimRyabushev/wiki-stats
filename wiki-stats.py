import os
import sys
import math

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


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
            self.vortexes = semi_vortexes
            self.names = names
            self.redirects = redirects
            self.sizes = sizes
            self.number_of_redirects =  articles_with_redirection      
        print('Граф загружен')
     
    def check(self):
         print(list(self.vortexes))
         print(list(self.edjes))
     
    def get_number_of_links_from(self, _id):
        return self.vertexes[_id]

    def get_links_from(self, k):
        return list(self.edjes[self.vortexes[k]:self.vortexes[k+1]])
        

    def get_id(self, title):
        for i in range(len(self.names)):
            if self.names[i] == title:
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
        return  min(self.vortexes[1:])
    
    def number_of_articles_with_minimal_links(self):
        minimal_links = self.minimal_links(self)
        couter = 0
        for i in self.vertexes:
            if i == minimal_links:
               counter += 1
        return counter
    
    def maximal_links(self):
        return  max(self.vortexes[1:])
    
    def number_of_articles_with_maximal_links(self):
        maximal_links = self.minimal_links(self)
        couter = 0
        for i in self.vertexes:
            if i == maximal_links:
               counter += 1
        return counter

    def article_with_maximal_links(self):
        maximal_links = self.minimal_links(self)
        for i in self.vertexes:
            if i == maximal_links:
               return self.get_title(i)
    


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл

name = '/home/student/wiki-stats/test'
wiki = WikiGraph(name)
print (wiki.get_page_size(0))
print (wiki.is_redirect(1))
print (wiki.get_title(0))
