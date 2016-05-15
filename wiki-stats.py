import os
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import array
import statistics

class Wiki:
    def __init__(self, filename):
        print('Загружаю граф из файла: ' + filename)
        with open(filename) as f:
            string = f.readline()
            string = string.rstrip().split()
            m = int(string[0])
            n = int(string[1])
            self.number_of_articles = m
            self.number_of_links = n
            offset = array.array('I', [0]*(m+1))
            edges = array.array('I', [1]*n)
            sizes = array.array('I', [0]*m)
            names = [' ' for i in range(m)]
            for index in range(1,m + 1):
                names[index - 1] = f.readline().rstrip()
                string = f.readline().rstrip().split()
                size, redirect, number_of_article = int(string[0]), int(string[1]), int(string[2])
                offset[index] = offset[index -1] + number_of_article
                sizes[index - 1] = size
                for i in range(number_of_article):
                    target = int(f.readline().rstrip())
                    edges[index - 1 + i] = target
        print('Граф загружен!')

   def get_links_from(self, k):
       return self.edges[self.offset[k]:self.offset[k+1]]

   def get_number_of_links_from(self, k):
       return self.offset[k+1]- self.offset[k]

   def get_id(self, name):
       index = 0
       while self.names[index] != name:
           index += 1
       return index

   def get_number_of_articles_with_exact_number_of_links(self, number):
       counter = 0
       for index in range(self.number_of_articles):
           if self.get_number_of_links_from(index) == number:
               counter += 1
       return counter

   def get_number_of_pages(self):
       return self.number_of_articles

   def is_redirect(self, k):
       if self.get_number_of_links_from(k) == 1:
           return True
       return False

   def get_name(self, k):
       return self.names[k]

   def get_size(self, k):
       return self.sizes[k]

   def get_number_of_redirects(self):
       counter = 0
       for i in range(self.number_of_articles):
           if self.is_redirect(i):
               counter += 1
       return counter

   def minimal_links(self):
       minimal = self.offset[-1]
       for i in range(self.number_of_articles):
           number = self.get_number_of_links_from(i)
           if number < minimal:
               minimal = number
       return minimal

   def get_number_of_articles_with_minimal_number_of_links(self):
       minimal = self.minimal_links()
       counter = 0
       for i in range(self.number_of_articles):
           if self.get_number_of_links_from(i) == minimal:
               counter += 1
       return counter

   def maximal_links(self):
       maximal = self.offset[-1]
       for i in range(self.number_of_articles):
          number = self.get_number_of_links_from(i)
          if number > maximal:
              maximal = number
       return maximal

   def get_number_of_articles_with_maximal_number_of_links(self):
       maximal = self.maximal_links()
       counter = 0
       for i in range(self.number_of_articles):
           if self.get_number_of_links_from(i) == maximal:
               counter += 1
       return counter

   def articles_with_maximal_links(self):
       maximal = self.maximal_links
       for i in range(self.number_of_articles):
           if self.get_number_of_links_from(i) == maximal:
               return self.get_name(i)

   def mean_number_of_links_from_article(self):
       number_of_links = []
       for i in range(self.number_of_articles):
           number_of_links.append(self.get_number_of_links_from(i))
       return statistics.mean(number_of_links)

   def links_to_article(self, k):
       answer = []
       for article in range(self.number_of_articles):
           if k in self.get_links_from(article):
               answer.append(article)
       return answer

   def number_of_links_to(self, vertex):
        return len(self.links_to_article(vertex))

   def minimal_number_of_outer_links(self):
       minimal = self.offset[-1]
       for i in range(self.number_of_articles):
           number = self.number_of_links_to(i)
           if  number < minimal:
               minimal = number
       return minimal

   def maximal_number_of_outer_links(self):
       maximal = 0
       for i in range(self.number_of_articles):
           number = self.number_of_links_to(i)
           if  number > maximal:
               maximal = number
       return maximal

   def number_of_articles_with_min_number_of_outer_links(self):
       minimal = self.minimal_number_of_outer_links()
       counter = 0
       for i in range(self.number_of_articles):
           if self.number_of_links_to(i) == minimal:
               counter += 1
       return counter

   def number_of_articles_with_max_number_of_outer_links(self):
       maximal = self.minimal_number_of_outer_links()
       counter = 0
       for i in range(self.number_of_articles):
           if self.number_of_links_to(i) == maximal:
               counter += 1
       return counter

   def article_with_min_number_of_outer_links(self):
       minimal = self.minimal_number_of_outer_links()
       for i in range(self.number_of_articles):
           if self.number_of_links_to(i) == minimal:
               return self.get_name(i)
               
