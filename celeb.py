#!/usr/bin/python
#-*- coding:utf-8 -*-
#明星问题概述：明星不认识任何人，然而所有人都认识他，请找出明星，G代表邻接矩阵
#该问题其实等价于处理某种依赖关系，可使用拓扑排序算法，但这里使用了一种更加巧妙的方法


def celeb(G):
    n=len(G)
    u,v=0,1
    #u代表第几个人，v代表u中邻接矩阵的位置
    for c in range(2,n+1):
        if G[u][v]:u=c
        #如果此时的u认识v，则u不为明星，因为任何人都认识明星，而此时v之前的人都可以确定不是明星，因为U不认识他们
        #v不变，依然代表现在可能为明星的人，而将c=v+1赋值给U，即v的下一个人，下一轮查看G[u][v]，看v下一个人是否认识他
        #如果认识，则U增加，继续检测，如果后面所有的人都认识v，那么v极有可能是明星，当然还需要检查v之前的人是否都认识他以及他是否不认识任何人

        #如果v之后有人不认识v，则说明这人可能是明星，而中间的人肯定不是明星，因为他们都认识v，而明星不认识任何一个人
        #这时候v=c，下一轮开始检测u中的邻接列表，从u之后的第一位邻居，也就是现在被赋值的v开始
        #重复上面的步骤，直至循环结束

        else:v=c
        #如果u不认识v，则将c赋值给v，检查u邻接矩阵下一位是否为真
    if u==n:c=v
    #如果u迭代到了最后，就是中间有一个v，他之后的人都认识他，才会导致这种结果，所以此时的v可能为明星
    else:c=u
    #否则就是u不认识他之后的所有，才会导致v一直增加，所以此时u可能为明星
    for v in range(n):
        #开始检查可能的人是否真是明星
        if c==v:continue
        if G[c][v]:break
        #如果认识别人
        if not G[v][c]:break
        #如果别人不认识他
    else:
    #循环结束执行else部分，返回明星
        return c
    return None
