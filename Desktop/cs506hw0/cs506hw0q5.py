import cs506hw0q3
import cs506hw0q2
import cs506hw0q1
X1=cs506hw0q1.import_data('C:\\Users\\dell\\Desktop\\cs506\\arrhythmia.data')
X2=cs506hw0q2.discard_missing(X1[0],X1[1])

#5a
def train_test_split(X,y,t_f):
    X3=cs506hw0q3.shuffle_data(X,y)     #import the random shuffle function in question 3a
    X_train=[]                          #shuffle X and y randomly
    y_train=[] 
    X_test=[]
    y_test=[]
    len_train=int(len(X3[0])*(1-t_f))   #calculation the len of train datset by using length*(1-t_f) amd the rest is the part for test
    X_train=X3[0][0:len_train]          #divide X and y in to X_train,y_train,X_test,y_test due to the portion calculated
    y_train=X3[1][0:len_train]
    X_test=X3[0][len_train:]
    y_test=X3[1][len_train:]
    # print(len(X_train))
    # print(len(X_test))
    return X_train,y_train,X_test,y_test
#test
train_test_split(X2[0],X2[1],0.2)

#5b
def train_test_CV_split(X,y,t_f,cv_f):
    X3=cs506hw0q3.shuffle_data(X,y)             #import the random shuffle function in question 3a
    X_train=[]                                  #shuffle X and y randomly
    y_train=[]
    X_test=[]
    y_test=[]
    X_cv=[]
    y_cv=[]
    len_test=int(len(X3[0])*t_f)                #Calculate the length fot test, cv, and the rest is for train
    len_cv=int(len(X3[0])*cv_f)
    X_test=X3[0][0:len_test]
    y_test=X3[1][0:len_test]
    X_cv=X3[0][len_test:len_cv+len_test]        #divide X and y in to X_train,y_train,X_test,y_test,X_cv,y_cv due to the portion calculated
    y_cv=X3[1][len_test:len_cv+len_test]
    X_train=X3[0][len_cv+len_test:]
    y_train=X3[1][len_cv+len_test:]
    # print(len(X_train))
    # print(len(X_test))
    # print(len(X_cv))
    return X_train,y_train,X_test,y_test,X_cv,y_cv
#test
train_test_CV_split(X2[0],X2[1],0.2,0.1)
