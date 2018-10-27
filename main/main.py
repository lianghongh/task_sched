from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score
from matplotlib import pyplot as plt

if __name__=='__main__':
    # 加载iris数据集
    iris = load_iris()
    X = iris.data
    y = iris.target

    k_range=range(1,31)
    k_scores=[]
    for k in k_range:
        knn=KNeighborsClassifier(k)
        scores=cross_val_score(knn,X,y,scoring="accuracy",cv=10)
        k_scores.append(scores.mean())


    kkk=sorted(zip(k_scores,k_range),key=lambda x:x[0],reverse=True)
    print("best k=%d" % kkk[0][1])
    knn=KNeighborsClassifier(kkk[0][1])
    knn.fit(X,y)
    print(knn.score(X,y),1,1,1)