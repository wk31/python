# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 22:41:47 2020

@author: 11597
"""

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def word_generate(frequency):
    wc = WordCloud(font_path='simkai.ttf', background_color='white', max_words=10, width=1920, height=1080, margin=5)
    wc.generate_from_frequencies(frequency)
    wc.to_file('market.png')
    plt.imshow(wc)
    plt.axis("off")
    plt.show()

#数据读取
data = pd.read_csv(r"Market_Basket_Optimisation.csv",header=None)
#数据处理缺失值
data.fillna(0, inplace=True)
#统计词频
saledict = pd.Series(dtype='float64')
for i in range(20):
    saledict = saledict.add(data[1].value_counts(), fill_value=0)
#处理缺失值词频
saledict.drop(saledict.index[0], inplace=True)

#生成词云
word_generate(saledict)


  
