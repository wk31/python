# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 22:00:00 2020

@author: 11597
"""

import requests
import time
import pandas as pd

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

#根目录
path_root = "https://lab.isaaclin.cn"
#数据总览地址
path_overall = path_root+"//nCoV//api//overall"
#数据地区地址
path_area = path_root+"//nCoV//api//provinceName"
#地区数据API
path_areadata= path_root+"//nCoV//api//area"


#数据概览
def get_overall():
    data_overall_json = requests.get(path_overall,headers=headers) 
    data_overall = data_overall_json.json()
    data_overall = data_overall['results'][0]
    return data_overall
    for key in data_overall.keys():
        print(key+': '+str(data_overall[key]))

#获取地区列表
def get_province_name():
    data_area_json = requests.get(path_area,headers=headers)
    data_area = data_area_json.json()
    data_area = data_area['results']
    return data_area
    for key in data_area:
        print(key)
        
#获取某个地区数据
def get_area_data(area):
    time.sleep(0.5)
    url = path_areadata+"?latest=1&province="+area
    data_json = requests.get(url,headers=headers)
    data = data_json.json()
    data = data["results"][0]
    return data
    print(data)
    
#获取世界数据
def get_worlddata():
    url = path_areadata+"?latest=1"
    data_json = requests.get(url,headers=headers)
    data = data_json.json()
    data = data["results"]
    return data
    print(data)
    


#get_overall()
#data_list = get_province_name()
    
#保存所有数据
def get_all_data():
    data = get_worlddata()
    datadict = pd.DataFrame(data)
    datadict.to_csv("./worlddata.csv")


#获取各省数据
def get_chinese_city_data():
    china_city = ["上海市", "云南省", "内蒙古自治区", "北京市", "台湾", "吉林省", "四川省", "天津市", "宁夏回族自治区", "安徽省", "山东省", "山西省", "广东省", "广西壮族自治区", "新疆维吾尔自治区", "江苏省", "江西省", "河北省", "河南省", "浙江省", "湖北省", "湖南省", "澳门", "甘肃省", "福建省", "西藏自治区", "贵州省", "辽宁省", "重庆市", "陕西省", "青海省", "香港", "黑龙江省"]
    result = [get_area_data('中国')]
    for key in china_city:
        print(key)
        data_city = get_area_data(key)
        result.append(data_city)
    data_city = pd.DataFrame(result)
    data_city.to_csv("./中国数据.csv")

#获取国外数据
def get_forign_data():
    china_city = ["上海市", "云南省", "内蒙古自治区", "北京市", "台湾", "吉林省", "四川省", "天津市", "宁夏回族自治区", "安徽省", "山东省", "山西省", "广东省", "广西壮族自治区", "新疆维吾尔自治区", "江苏省", "江西省", "河北省", "河南省", "浙江省", "湖北省", "湖南省", "澳门", "甘肃省", "福建省", "西藏自治区", "贵州省", "辽宁省", "重庆市", "陕西省", "青海省", "香港", "黑龙江省"]
    city = get_province_name()
    result = []
    for key in china_city:
        city.remove(key)
    for key in city:
        print(key)
        data_city = get_area_data(key)
        result.append(data_city)
    data_city = pd.DataFrame(result)
    data_city.to_csv("./国外数据.csv")

get_all_data()
get_chinese_city_data()
get_forign_data()
    


