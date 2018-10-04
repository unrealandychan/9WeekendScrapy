import word2vec

word2vec.word2vec("plain_text.txt","plain_text.bin",size = 300,verbose=True)

model = word2vec.load("plain_text.bin")
for i in range(100):
    print(model.vocab[-i])
    
indexes = model.cosine(u'作者') 
for index in indexes[0]:
    print(model.vocab[index])