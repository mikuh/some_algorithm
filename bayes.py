from numpy import *

#原始数据和标注
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec


#创建词汇表
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

mydata,classVec = loadDataSet()

vocabList = createVocabList(mydata)



#句子转向量
def setOfWords2Vec(vocabList,inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

sVec = [setOfWords2Vec(vocabList,inputset) for inputset in mydata]


#贝叶斯分类器训练函数
#输入参数是文档向量矩阵、每篇文档类别标签
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)  #参与训练的文档数
    numWords = len(trainMatrix[0])   #特征数量
    pAbusive = sum(trainCategory)/float(numTrainDocs)  #每篇文档属于侮辱性文档的概率
    p0Num = ones(numWords)     #初始化都为1的矩阵 防止出现词汇概率0
    p1Num = ones(numWords)      #初始化都为1的矩阵
    p0Denom = 2.0   #初始化为2 因为侮辱句和非侮辱句概率为0.5
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i] #侮辱句向量相加
            p1Denom += sum(trainMatrix[i])  #侮辱句词汇数量相加
        else:
            p0Num += trainMatrix[i] #非侮辱句向量相加
            p0Denom += sum(trainMatrix[i]) #非侮辱句词汇数量相加
    p1Vect = log(p1Num/p1Denom)          # 防止概率过小 取对数，跟后面贝叶斯公式计算概率对应
    p0Vect = log(p0Num/p0Denom)
    # p1Vect = p1Num / p1Denom  # 侮辱句子向量和/总得侮辱句中的词汇数量= 侮辱句中 每个词出现的概率
    # p0Vect = p0Num / p0Denom  # 非侮辱句中每个词出现的概率
    return p0Vect,p1Vect,pAbusive

p0Vec,p1Vec,pAbusive = trainNB0(sVec,classVec)


#朴素贝叶斯分类函数
#输入参数为 要分类的向量、以及上面函数计算得到的三个概率
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)    #根据贝叶斯公式计算是侮辱性句子的概率
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))

testingNB()
