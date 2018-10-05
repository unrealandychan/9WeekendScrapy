# -*- coding: utf-8 -*-

from gensim.models import word2vec

sentences = word2vec.LineSentence("plain_text.txt")
model = word2vec.Word2Vec(sentences,size = 300 ,min_count = 5 )
model.save("w2v.model")


model.wv.distance("香港","蛋糕")

print(model.wv.similar_by_word("朱古力"))