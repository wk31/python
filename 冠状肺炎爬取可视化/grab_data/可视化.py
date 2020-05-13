# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:53:54 2020

@author: 11597
"""
import matplotlib
import matplotlib.pyplot as plt
import seaborn as seaborn
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


data = pd.read_csv(r"F:\tensorflow项目\数据分析与python基础\练习\L3\肺炎\数仓\DXY-COVID-19-Data-master\csv\DXYArea.csv")
china_data = pd.read_csv(r"F:\tensorflow项目\数据分析与python基础\练习\L3\肺炎\grab_data\中国数据.csv")
#各省市变化曲线
def plot_province(province):
    datachina = data[data.provinceName==province]
    #datachina[['updateTime']] = datachina[['updateTime']].apply(pd.to_datetime)
    datachina['updateTime']=pd.to_datetime(datachina['updateTime']) 
    print(type(datachina['updateTime'].iloc[1]))
    datachina = datachina.resample('1D', on='updateTime').last()
    
    plt.figure(figsize=(8,6))
    plt.plot(datachina['province_confirmedCount'],'r',label="confirm")
    plt.plot(datachina['province_curedCount'],'g', label="cured")
    plt.plot(datachina['province_deadCount'],'gray', label="dead")
    plt.plot(datachina['province_confirmedCount']-datachina['province_curedCount']-datachina['province_deadCount'],'C1', label="now")
    plt.ylim(0,datachina['province_confirmedCount'].max(axis=0) * 1.2)
    plt.legend()
    plt.xticks(rotation=45)
    plt.xlabel("日期",  fontsize='large')
    plt.ylabel("人数", fontsize='large')
    plt.title(province+" 数据")
    plt.show()

plot_province("北京市")

#各省市治愈，死亡占比
def plot_pie(province):
    labels = 'cured','dead','now'
    piedata = []
    cured=china_data[china_data.provinceName==province].iloc[0]["curedCount"]
    confirm=china_data[china_data.provinceName==province].iloc[0]["confirmedCount"]
    die=china_data[china_data.provinceName==province].iloc[0]["deadCount"]
    now=confirm-cured-die
    piedata.append(cured)
    #piedata.append(confirm)
    piedata.append(die)
    piedata.append(now)
    plt.figure(figsize=(8,8))
    plt.pie(piedata,labels=labels,autopct='%1.1f%%',startangle=90,shadow=True)

plot_pie("北京市")


#除去湖北其它省市确诊数量
def plot_bar():
    bar_width = 0.35
    opacity = 0.4
    data_other = china_data[china_data["provinceName"] != "中国" ]
    data_other = data_other[data_other["provinceName"] != "湖北省"  ]
    confirmed = data_other["confirmedCount"]
    city = data_other["provinceName"]
#    num = data_other.shape[0]
    plt.figure(figsize=(18,6))
#    fig,ax = plt.subplots()
    plt.bar(city, confirmed, bar_width,
                        alpha=opacity, color='b',
                        label='Men')
    plt.xticks(rotation=45)
    
plot_bar()

    