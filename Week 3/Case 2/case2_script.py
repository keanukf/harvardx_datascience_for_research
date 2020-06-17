#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:16:28 2020

@author: kforthmann
"""

from collections import Counter

text  = "This is my test text. I keep it short to keep things managable."

def count_words(text):
    text = text.lower()
    skips = [",",".",":",";","'",'"']
    
    for ch in skips:   
        text = text.replace(ch,"")
    
    
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def count_words_fast(text):
    text = text.lower()
    skips = [",",".",":",";","'",'"']
    
    for ch in skips:   
        text = text.replace(ch,"")
    
    
    word_counts = Counter(text.split(" "))
    return word_counts


def read_book(title_path):
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n","").replace("\r","")        
    return text


def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)
