# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 23:33:29 2020

@author: 11597
"""

import requests
import re
import numpy as np
import json
from functools import reduce
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
r = requests.get('http://map.amap.com/service/subway?_1469083453978&srhdata=1100_drw_beijing.json')
ll='1'
def get_lines_stations_info(text):
#    线路和站点
    splitText = re.split('"ln":"(\w+)"',  text) 
    xl = []
    zd = []
    zb = []
    lines_info = {}
    for t in splitText:
        m = re.findall('"kn":"(\w+)"',  t) 
        n = re.findall('"n":"(\w+)"',  t)
        if m:xl.append(m)
        if n:zd.append(n)
    for i in range(len(xl)):
        lines_info[xl[i][0]] = zd[i]
    
    allzd = reduce(lambda x, y: x+y, zd)
#    print(allzd, len(allzd))
    zb = re.findall('"sl":"(\d+.\d+),(\d+.\d+)"',text)
    zb = [list(x) for x in zb]
    zbf = []
    for i in zb:
        zbf.append([float(x) for x in i])
        
    stations_info = {}
    stations_info = dict(zip(allzd, zbf))
#    print(stations_info)
    
    return lines_info, stations_info

    
lines_info=get_lines_stations_info(r.text)
    


from collections import defaultdict
def get_neighbor_info(lines_info):
    lines = lines_info[0]
    neighbor_info = defaultdict(list)
    for line in lines.keys():
        allzd = lines[line]
        neighbor_info[allzd[0]].append(allzd[1])
        neighbor_info[allzd[len(allzd)-1]].append(allzd[len(allzd)-2])
        for i in range(1,len(allzd)-1):
            neighbor_info[allzd[i]].append(allzd[i+1])
            neighbor_info[allzd[i]].append(allzd[i-1])
        if (line =='地铁10号线')or(line =='地铁2号线'):
            neighbor_info[allzd[0]].append(allzd[len(allzd)-1])
            neighbor_info[allzd[len(allzd)-1]].append(allzd[0])
        
    return neighbor_info
        
neighbor_info = get_neighbor_info(lines_info)





#画地图
for x in lines_info[1].keys():
    lines_info[1][x][0] = (lines_info[1][x][0]-116)*10
    lines_info[1][x][1] = (lines_info[1][x][1]-39)*10

plt.figure(figsize=(60, 60))
city_graph = nx.Graph()
city_graph.add_nodes_from(list(lines_info[1].keys()))
nx.draw(city_graph, lines_info[1], with_labels=True, node_size=20)
plt.savefig('dt1.png')

cities_connection_graph = nx.Graph(neighbor_info)
nx.draw(cities_connection_graph,lines_info[1],with_labels=True,node_size=10)


'''
# 你可以用递归查找所有路径
def get_path_DFS_ALL(lines_info, neighbor_info, from_station, to_station):
    # 递归算法，本质上是深度优先
    # 遍历所有路径
    # 这种情况下，站点间的坐标距离难以转化为可靠的启发函数，所以只用简单的BFS算法
    # 检查输入站点名称
    need_search_station = [[from_station]]
    all_paths = []

    while len(all_paths) < 3:
        path = need_search_station.pop(-1)
        ## 获取路径最远端的节点
        end_node = path[-1]
        ## 通过最远端的节点，查找其关联的节点
        expend_node = neighbor_info[end_node]
        #print(expend_node)
        ## 遍历关联节点列表，将原来路径和新节点组合成新路径
        for node in expend_node:
            if node in path: continue
            new_path = path + [node]
            #print('new path: {}'.format(new_path))
            need_search_station.append(new_path)
            if node == to_station:
                all_paths.append(new_path)
    return all_paths
    
result = get_path_DFS_ALL(lines_info, neighbor_info, "北京站", "北京西站") 
print(result)
'''
'''
def get_path_DFS_ALL(lines_info, neighbor_info, from_station, to_station):
    # 递归算法，本质上是深度优先
    # 遍历所有路径
    # 这种情况下，站点间的坐标距离难以转化为可靠的启发函数，所以只用简单的BFS算法
    # 检查输入站点名称
    reasult = []
    pathes = [[from_station]]
    visited = set()
    
    while pathes:
        path = pathes.pop(0)
        froniter = path[-1]
        
        if froniter in visited: continue
            
        successsors = neighbor_info[froniter]
        
        for city in successsors:
            if city in path: continue  # check loop
            
            new_path = path+[city]
#            pathes.append(new_path)  #bfs
            pathes = [new_path] + pathes #dfs
            
#            print(new_path)
            if city == to_station:
                reasult.append(new_path)
#                return new_path
        visited.add(froniter)
    
    return reasult        
print(get_path_DFS_ALL(lines_info, neighbor_info, "北京站", "北京西站" ))
'''


def get_path_DFS_ALL(lines_info, neighbor_info, from_station, to_station):
    pathes = [[from_station]]
    #visited = set()
    path = [[]]
    while pathes:
        path = pathes.pop(0)
        froniter = path[-1]
        #if froniter in visited : continue
        #if froniter == destination:
        #    return path
        successsors = neighbor_info[froniter]
        
        for city in successsors:
            if city in path: continue  # check loop
            
            new_path = path+[city]
            
            pathes.append(new_path)  #bfs
            
#        pathes = search_strategy(pathes)
       # visited.add(froniter)
        if pathes and (to_station == pathes[0][-1]):
            return pathes[0]

print(get_path_DFS_ALL(lines_info, neighbor_info, "育新", "北京西站" ))
















