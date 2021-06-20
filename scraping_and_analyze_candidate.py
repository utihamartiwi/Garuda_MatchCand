# -*- coding: utf-8 -*-
"""scraping and analyze candidate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12Tf85-QNu3wAzBDCAvkkZDSQzpKEJTjp
"""

!pip install beautifulsoup4
!pip install requests

from bs4 import BeautifulSoup
import random
import argparse
import requests
import re
import pandas as pd
import numpy as np
import time

class LinkedinScraper(object):
    def __init__(self, keyword, limit, lim_2):
        """
        :param keyword: a str of keyword(s) to search for
        :param limit: number of profiles to scrape
        """
        self.keyword = keyword.replace(' ', '%20')
        self.all_htmls = ""
        self.server = 'www.google.com'
        self.quantity = '100'
        self.limit = int(limit)
        self.lim_2 = int(lim_2)
        self.counter = 0

    def search(self):
        """
        perform the search
        :return: a list of htmls from Google Searches
        """

        while self.counter < self.limit:
            headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205'}
            url = 'http://google.com/search?num=100&start=' + str(self.counter) + '&hl=en&meta=&q=site%3Alinkedin.com/in%20' + self.keyword
            resp = requests.get(url, headers=headers)
            soup = BeautifulSoup(resp.content, "html.parser")
          
            if ("Our systems have detected unusual traffic from your computer network.") in resp.text:
                print("Running into captchas")
                return

            self.all_htmls += resp.text
            self.counter += 100

    def parse_links(self):
        reg_links = re.compile(r"url=https:\/\/www\.linkedin.com(.*?)&")
        self.temp = reg_links.findall(self.all_htmls)
        results = []
        for regex in self.temp:
            final_url = regex.replace("url=", "")
            #print(final_url)
            results.append("https://www.linkedin.com" + final_url)
        return results


    def parse_people(self):
        """
        :param html: parse the html for Linkedin Profiles using regex
        :return: a list of
        """
        reg_people = re.compile(r'">[a-zA-Z0-9._ -]* -|\| LinkedIn')
        self.temp = reg_people.findall(self.all_htmls)
        results = []
        r_git = []
        for iteration in (self.temp):
            delete = iteration.replace(' | LinkedIn', '')
            delete = delete.replace(' - LinkedIn', '')
            delete = delete.replace(' profiles ', '')
            delete = delete.replace('LinkedIn', '')
            delete = delete.replace('"', '')
            delete = delete.replace('>', '')
            delete = delete.replace('| ', " ")
            delete = delete.strip("-")
            if delete != " ":
                results.append(delete)
        nn = []
        pp = []
        for p in results[:self.lim_2]:
          name = p.split('-')
          nn.append(name[0])
          if len(name) == 1:
            pp.append('-')
          else:
            pp.append(name[1])
          all_htmls1 = ""
          url1 = 'http://google.com/search?num=100&start=0&hl=en&meta=&q=site%3Agithub.com/%20' + name[0]
          headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205'}
          resp1 = requests.get(url1, headers=headers)
          all_htmls1 += resp1.text
          reg_links1 = re.compile(r"url=https://github.com(.*?)&")
          temp1 = reg_links1.findall(all_htmls1)
          if len(temp1) == 0:
            r_git.append(temp1)
            
          else:
              final_url = temp1[0].replace("url=", "")
              r_git.append("https://github.com" + final_url)
            
        return nn, pp, r_git

n_result = 20
keyword = "data scientist"
start = time.time()
df = pd.DataFrame()
ls = LinkedinScraper(keyword=keyword,limit=1, lim_2=n_result)
ls.search()
links = ls.parse_links()
name, prof, gitpr = ls.parse_people()
end = time.time()
print('it takes time = ', end - start, 's')
df['name'] = name
df['skill/job'] = prof
df['linkedin-link'] = links[:n_result]
df['github'] = gitpr
df.to_csv('prospoctive candidate.csv')
df

HR_need = pd.read_csv('HR data.csv')
HR_need

cand = pd.read_csv('candidate.csv')
cand

#Convert level to number
def lev(what, form_):
  list_level = []
  for i in form_[what]:
    if i == 'Bachelor' or i == 'Low':
      list_level.append(1)
    elif i == 'Master' or i == 'Medium':
      list_level.append(2)
    elif i == 'Doctor' or i == 'High':
      list_level.append(3)
    else:
      list_level.append(0)
  form_['newlevel_'+ what] = list_level

lev('Level of education', HR_need)
lev('Level_skill1', HR_need)
lev('Level_skill2', HR_need)
lev('Level_Skill3', HR_need)

lev('Level of education', cand)
lev('Level_1', cand)
lev('Level_2', cand)
lev('Level_3', cand)

def match(job, top):
  match = []
  add_score = []
  dc = cand[cand['Position'] == job]
  ind = list(range(len(dc)))
  dc.index = ind
  dh = HR_need[HR_need['Position'] == job]
  skillHR_list = [dh['Skill_1'].values[0], dh['Skill_2'].values[0], dh['Skill_3'].values[0]]
  levelHR_list = [dh['newlevel_Level_skill1'].values[0], dh['newlevel_Level_skill2'].values[0], dh['newlevel_Level_Skill3'].values[0]]
  el = int(dh['newlevel_Level of education'].values[0])
  exh = int(dh['Related_Experience'].values[0])
  ch = dh['City'].values[0]

  for i in range(len(dc)):
    m = 0
    s = 0
    edc = dc['newlevel_Level of education'][i]
    if edc >= el:
      m = m + 1
      s = s + (edc - el)

    if dc['field'][i] == dh['field'].values[0]:
      m = m + 1
    
    #skill
    skillcan_list = [dc['Skill1'][i], dc['Skill2'][i], dc['Skill3'][i]]
    levelcan_list = [dc['newlevel_Level_1'][i], dc['newlevel_Level_2'][i], dc['newlevel_Level_3'][i]]

    for j, skill_ in enumerate(skillHR_list):
      if str(skill_) in skillcan_list:
        m = m + 1
        if levelcan_list[skillcan_list.index(skill_)] >= levelHR_list[j]:
          m = m+1
          s = s + (levelcan_list[skillcan_list.index(skill_)] - levelHR_list[j])
          
    #experience
    exc = int(dc['Related_Experience'][i])
    if exc >= exh:
      m = m + 1
      s = s + (exc - exh)
    
    #city
    if dc['City'][i] == ch:
      m = m+1
    
    match.append(m*10)
    add_score.append(s*10)
  dc['match'] = match
  dc['add_score'] = add_score
  d_sort = dc.sort_values(by=['match', 'add_score'], ascending=False)
  dtop = d_sort.head(top)

  df = pd.DataFrame({'match': dtop['match'].values,
                   'add_score': dtop['add_score'].values}, index=dtop['Name'].values)
  ax = df.plot.bar(stacked=True)

  return d_sort, dtop

df_all, df_top = match('data scientist', 5)
df_top

