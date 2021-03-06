#!/usr/bin/python
#-*- coding:utf-8 -*-
#深度优先搜索算法
#一直深入，直到进入死胡同，则回溯到上一个路由，选择另外一条
#当然这是理解思路，实现起来会换一种方式，使用递归调用来模仿一直深入
#直到没有路（子节点）可以选择，递归终止返回上一级，模仿回溯过程

#递归版深度优先搜索算法
def rec_dfs(G,s,S=None):
    if S is None:S=set()
    #S记录访问过的节点
    S.add(s)
    #添加根节点
    for u in G[s]:
        #迭代s邻居，但此时只会进行第一次循环，第一次循环中递归调用到下一级，该循环并没有完成
        if u in S:continue
        rec_dfs(G,u,S)
        #传入已访问过节点列表S，递归调用继续深入
        #如果没有字节点，则递归完成返回上一级，执行下一个循环，即递归另一个字节点

#迭代版深度优先搜索算法
def iter_dfs(G,s):
    S,Q=set(),[]
    #S为访问过的节点
    Q.append(s)
    while Q:
        u=Q.pop()
        #pop推出列表右边的元素，所以是后进先出，于是遍历一直深入
        #pop完一层字节点后，才轮到上一层节点，所以也与回溯过程相似
        if u in S:continue
        #如果访问过
        S.add(u)
        #添加到访问过的列表
        Q.extend(G[u])
        #Q添加u字节点
        yield u

#带时间戳的深度优先搜索
#为每个节点添加发现时的时间，以及回溯时的时间
def dsf(G,s,d,f,S=None,t=0):
    if S is None:S=set()
    d[s]=t
    #设置发现时间
    t+=1
    #时间t加1
    S.add(s)
    #加入访问过的节点
    for u in G[s]:
    #循环迭代当前节点字节点进行遍历
        if u in S:continue
        t=dsf(G,u,d,f,s,t)
        f[s]=t
        t+=1
        return t
    #与深度优先算法一样，循环只会执行一次，然后递归深入下一层，直到叶节点回溯上一层
    #同时设置叶节点回溯时间f[s]，返回t+1到上一层的循环中，循环中将返回值赋给t，然后进行下一轮循环，或者返回上一级

#迭代深度的深度优先搜索
#如果图规模很大，无法短时间采用深度优先算法遍历完，而且你仅仅想遍历一个范围内的所有节点
#可以使用该算法，该算法设定了一个范围值，每次递归都减少一次，当数值为零则停止递归
def iddfs(G,s):
    yielded=set()
    #访问过的节点
    def recurse(G,s,d,S=None):
        if s not in yielded:
            yield s
            #如果s没有访问过
            yielded.add(s)
        if d==0:return
        #范围计数为零
        if S is None:S=set()
        S.add(s)
        #该次递归记录访问过的节点
        for u in G[s]:
            if u in S:continue
            for v in recurse(G,u,d-1,S):
            #开始递归，递归到下层，下层节点首先yield自身，然后也进行循环递归
            #当一次循环完成后，会得到子节点的所有子节点，然后全部yield到上级，然后循环另一个字节点
            #所以每次递归都能保证获得下层所有节点信息
                yield v
    n=len(G)
    for d in range(n):
        #在G长度内循环，直到遍历完所有节点
        if len(yielded)==n:break
        for u in recurse(G,s,d):
            yield u

