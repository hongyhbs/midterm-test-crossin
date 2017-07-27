#coding:utf-8
#1\打开文件并读取
import csv
with open('report.txt') as f:
    first_line = f.readline()

    first_line = '名次 ' + first_line.strip()+ '总分 ' + '平均分 \n'
    print first_line
    with open('scores_order.txt','w') as w:
        w.write(first_line)
    lines = f.readlines()




#name = raw_input('输入查询名字')

#2\分割开列表，然后统计

scores = []    #分数的空字典 key = name
scores_ave = []  #每个人平均分的空字典  key = name ,value = score
sum_ave1 =[]       #以下是各科平均分的空列表 ave1代表第一个科目
sum_ave2 =[]
sum_ave3 =[]
sum_ave4 =[]
sum_ave5 =[]
sum_ave6 =[]
sum_ave7 =[]
sum_ave8 =[]
sum_ave9 =[]
n = 0 #计数器，计算有几个科目
for i in lines[1:]:   #去掉第一行
    s = i.split()

#这时，line中的元素都是字符串，需要转换。先实现目的，不管方式优化
    k1 = float(s[1])
    k2 = float(s[2])
    k3 = float(s[3])
    k4 = float(s[4])
    k5 = float(s[5])
    k6 = float(s[6])
    k7 = float(s[7])
    k8 = float(s[8])
    k9 = float(s[9])
#求每个人的平均分
#这里有个问题，每次只吧最后的值写进字典，没有全部写入字典.需要把字典初始化
#放在循环的外面
    # 求取每一个科目的平均分
    k_sum = k1 + k2 + k3 + k4 + k5 + k6 + k7 + k8 + k9
    k_ave = float(k_sum)/9 #每个人的平均分
         #每个人的总分
    s.append(k_sum)
    s.append(k_ave)


    sum_ave1.append(s[1])
    n += 1  #计算有多少个人参与了统计
    sum_ave2.append(s[2])
    sum_ave3.append(s[3])
    sum_ave4.append(s[4])
    sum_ave5.append(s[5])
    sum_ave6.append(s[6])
    sum_ave7.append(s[7])
    sum_ave8.append(s[8])
    sum_ave9.append(s[9])



#把分数放进字典里




    #求出每一个科目的全班平均分
    x0 = []
    a1 = [int(x) for x in sum_ave1]
    a2 = [int(x) for x in sum_ave2]
    a3 = [int(x) for x in sum_ave3]
    a4 = [int(x) for x in sum_ave4]
    a5 = [int(x) for x in sum_ave5]
    a6 = [int(x) for x in sum_ave6]
    a7 = [int(x) for x in sum_ave7]
    a8 = [int(x) for x in sum_ave8]
    a9 = [int(x) for x in sum_ave9]


    x1 = sum(a1[0:])/n
    x2 = sum(a2[0:])/n
    x3 = sum(a3[0:])/n
    x4 = sum(a4[0:])/n
    x5 = sum(a5[0:])/n
    x6 = sum(a6[0:])/n
    x7 = sum(a7[0:])/n
    x8 = sum(a8[0:])/n
    x9 = sum(a9[0:])/n

    x0.append(x1)
    x0.append(x2)
    x0.append(x3)
    x0.append(x4)
    x0.append(x5)
    x0.append(x6)
    x0.append(x7)
    x0.append(x8)
    x0.append(x9)
    x_sum = float(x1+x2+x3+x4+x5+x6+x7+x8+x9)
    x_ave =x_sum/9
    x0.append(x_sum)   #x0：全班的所有科目平均分和总分，及全班的总分平均分。列表形式
    x0.append(x_ave)
    #print x0
    ##实现统计各科的平均分数 待写入文档
    #print scores
    scores.append(s)
#sorted函数不产生新的列表，所以要重新赋值
scores = sorted(scores, key = lambda x:x[-1],reverse = True)

#用平均分数排定名次--列表下
j = 0
for i in scores:

    j += 1
    i.insert(0,j) #i 是列表，可以直接使用insert，但不可以split



print scores
f = open('scores_order.txt','a+')
for i in scores :
    i = str(i) + '\n'
    f.write(i)
f.close()
###***********下面开始替换*********

#*********替换暂时解决不了，要么先写入文件，然后再读取出来变成字符串然后再替换？




#这里应该要把字典里的内容转化为有序的list，然后进行比较
#考虑到还要在最前面加1个排名，最后应该是要把字典变成list写入
#1、先完成有序排列

###把字典转为列表来排序






#score = scores.get(name)
#if score is None:
#    score=[0,0,0,0,0,0,0,0,0]
#print score








