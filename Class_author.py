import pandas as pd
import  numpy as np
from KPL_Class import  kpl
import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
import math
import time
import os

class Author:
    def __init__(self,name_):
        self.coauthor_nameSet = set()
        self.coauthor_instanceDict = {}
        self.coauthor_title_set = set()
        self.institute_set = set()
        self.name = name_
        self.title_set = set()
        self.reserve_remove_flag_forStep1 = 1    
        self.reserve_remove_flag_forStep3 = 1   
        self.reserve_remove_flag_forStep5 = 1 
        self.year_set = set()
        self.id_1 = 0
        self.id1_set = set()

    def add_coauthor_name(self,coauthor_):   
        self.coauthor_nameSet.add(coauthor_)
    def add_coauthorInstanceDict(self,name_,instance_):
        self.coauthor_instanceDict[name_] = instance_
    def add_coauthor_title_set(self,title_author):
        self.coauthor_title_set.add(title_author)
    def add_institute(self, institute_):
        self.institute_set.add(institute_)
    def setId_1(self, idx):
        self.id_1 = idx
    def set_name(self,name_):
        self.name = name_
    def add_id_set(self,idx):
        self.id1_set.add(idx)
    def add_title(self,title_):
        self.title_set.add(title_)
    def add_year(self,year_):
        self.year_set.add(year_)
    def drop_author_name(self,author_):
        self.coauthor_nameSet.remove(author_)
    def drop_author_instance_dict(self,author_name):
        self.coauthor_instanceDict.pop(author_name)
    def remove_step1(self):
        self.reserve_remove_flag_forStep1 = 0
    def remove_step3(self):
        self.reserve_remove_flag_forStep3 = 0
    def remove_step5(self):
        self.reserve_remove_flag_forStep5 = 0
    def get_coauthor_nameSet(self):
        return self.coauthor_nameSet
    def get_coauthor_instanceDict(self):
        return self.coauthor_instanceDict
    def get_coauthor_titleSet(self):
        return self.coauthor_title_set
    def get_firstName(self):
        return self.name.split(', ')[0]
    def get_instituteSet(self):
        return self.institute_set
    def getId_1(self):
        return self.id_1
    def get_id_set(self):
        return self.id1_set
    def get_name(self):
        return self.name
    def get_secondName(self):
        try:
            return self.name.split(', ')[1]
        except:
            return ''
    def get_reserve_remove_flag_forStep1(self):
        return self.reserve_remove_flag_forStep1
    def get_reserve_remove_flag_forStep3(self):
        return self.reserve_remove_flag_forStep3
    def get_reserve_remove_flag_forStep5(self):
        return self.reserve_remove_flag_forStep5
    def get_titleSet(self):
        return self.title_set
    def get_yearSet(self):
        return self.year_set
    def merge(self,author2):
        coauthor_nameSet2 = author2.get_coauthor_nameSet()
        title_set2 = author2.get_titleSet()
        institute_set2 = author2.get_instituteSet()
        coauthor_title_set2 = author2.get_coauthor_titleSet()
        yearSet2= author2.get_yearSet()
        id1_set_2 = author2.get_id_set()
        self.coauthor_nameSet = self.coauthor_nameSet.union(coauthor_nameSet2)
        self.title_set = self.title_set.union(title_set2)
        self.institute_set = self.institute_set.union(institute_set2)
        self.coauthor_title_set = self.coauthor_title_set.union(coauthor_title_set2)
        self.year_set = self.year_set.union(yearSet2)
        self.id1_set = self.id1_set.union(id1_set_2)

