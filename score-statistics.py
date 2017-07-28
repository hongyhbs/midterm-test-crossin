#coding:utf-8
#*********首先把文档里的内容变成可以处理的类型（type），然后开始处理***********
with open('report.txt','r') as f:
    lines = f.readlines()  #首先取出所有的行数据，每一行生成一个字符串。
    #现在要把字符串改成单独的列表。
single_score = []  #需要一个存放每个人成绩的工具，空列表,这个列表需要在循环之外，否则每次都清零了

total_sum = 0 #存放全班各科总成绩的变量
k1 = 0.0        #计算全班人数的变量
k2 = 1
total_score = []
for line in lines:
    # *****************处理全班的平均分问题********************
#把全班的各科平均分求出来，放进一个新列表里，作为第一项，这样写入的时候就不用单独写了

    s = line.split()
    while k2 <= 9:
        total_sum += int(s[k2])
        k1 += 1
        k2 += 1
        total_ave = total_sum / k1
        total_score.append(round(total_ave, 2))

#total_ave = total_sum/k1
#total_score.append(round(total_ave,2))
m = 0
for k_3 in total_score :
    m += k_3
m1 = m/9.0

total_score.append(m)
total_score.append(round(m1,2))
total_score.insert(0,'平均')
total_score.insert(0,0)






for line in lines:
    # *****************处理全班的平均分问题********************
    sum = 0  #需要一个存放成绩的空变量

    k = 0.0   #需要一个计数器，计算有几门科目
    i = line.split()



    for w in i[1:]:
        sum += int(w)
        k += 1
        sum_ave = round(sum/k,2)

    i.append(sum)
    i.append(sum_ave)
    single_score.append(i)




    #*************处理完成，开始排序**********88
single_score.sort(key = lambda  x :x[11],reverse = True )

m = 1
for i in single_score :
    i.insert(0,m)
    m += 1
print single_score


