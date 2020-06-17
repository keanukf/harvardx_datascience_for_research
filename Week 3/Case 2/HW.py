#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 21:01:53 2020

@author: kforthmann
"""


import os 
import pandas as pd 
import numpy as np 
from collections import Counter
def count_words_fast(text): 
    text = text.lower() 
    skips = [".", ",", ";", ":", "'", '"', "\n", "!", "?", "(", ")"] 
    for ch in skips: 
        text = text.replace(ch, "") 
    word_counts = Counter(text.split(" ")) 
    return word_counts
def read_book(title_path): 
    text   = pd.read_csv(title_path, sep = "\n", engine='python', encoding="utf8") 
    text = text.to_string(index = False) 
    return text
def word_stats(word_counts): 
    num_unique = len(word_counts) 
    counts = word_counts.values() 
    return (num_unique, counts)