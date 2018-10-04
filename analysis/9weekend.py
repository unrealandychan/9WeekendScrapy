# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import jieba
import word2vec
import re

#先把資料準備好，利用 2017 － 2018 的全部資料
df = pd.read_csv("weekend_food_with_tag.csv")
dataset= df[df["Date"]>'2017']

tags= []
keywords = {}


#Helping Functions 
def splitTag():
    for i in dataset["Tag"]:
        j = str(i).split(",")
        for x in j:
            if x not in tags:
                tags.append(x)
                
def makeTagDict():
    for i in dataset['Tag']:
        j = str(i).split(",")
        for word in j:
            if word not in keywords.keys():
                keywords[str(word)] = 1
            else:
                keywords[str(word)] +=1
            
sort_key = sorted(keywords.items(),key = lambda x:x[1],reverse = True)



count = 0

for word in dataset["Content"].values:
    
    if "膽固醇" in str(word):
        count+=1
print(count)
    

    
sug_word = ["馬鞍山","八爪魚","食肉獸","肉眼扒","製作","好唔好","唔好","西柚","入手","跡象","瘋狂",
            "即食麵","深水埗","現正","絕對","旺角","尖沙嘴","自製","打卡","文青",'歷史',"班戟","慾望",
            "陳皮","麵廠","一粒粒","雞爪凍","係咩","太安樓","片皮鴨","對抗",'薑茶','紅豆','邪惡','隱世',
            '大多數','忌廉','朱古力','榴槤','黑白','即日','後製','至上','新傳媒']

for k in sug_word:
    jieba.add_word(k)
    
file_train_Seg = []

for key in dataset['Content']:
    file_train_Seg.append(' '.join(list(jieba.cut(str(key),cut_all = False))))

for i in range(len(file_train_Seg)):
    file_train_Seg[i] = re.sub(r',|。|！|（|）|，|✓|\n|\xa0|：|…|;|＄|／|；|、|「|」|•|</s>|』','',file_train_Seg[i])
    file_train_Seg[i] = re.sub(r'了|媽|的|呢|有|亦|但|而|除|都|畀|因為|所以|和|及|以|如下|係|做|備|又|也|於|在|是|就|更|嘅|與|Text|photo|text|Edit','',file_train_Seg[i])
    file_train_Seg[i] = re.sub(r'\d{0,8}','',file_train_Seg[i])
    
print(file_train_Seg)
    
plain_text = 'plain_text.txt'

with open(plain_text ,'wb') as txt:
    for i in file_train_Seg:
        txt.write(i.encode('utf-8'))
        txt.write(b'\n')

