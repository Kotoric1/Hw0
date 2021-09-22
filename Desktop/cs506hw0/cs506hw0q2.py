import cs506hw0q1

X1=cs506hw0q1.import_data('C:\\Users\\dell\\Desktop\\cs506\\arrhythmia.data') #import data from question 1
# 2a
def impute_missing(X):
    k=0               
    # print(len(X))
    for k in range (279):   #replace by column
        new_X=[]            #initial settings
        c=0
        for c in range (len(X)):    #deletes the "NaN"s and copy everything else
            if X[c][k] != 'NaN':
                new_X.append(X[c][k])
            c=c+1
        # print(new_X)
        # print(len(new_X))
        if len(new_X)%2 == 1:                   #find the median by odd or even length
            median= float(new_X[int((len(new_X)+1)/2)])
        else:
            median=(float(new_X[int(len(new_X)/2)])+float(new_X[int(len(new_X)/2)+1]))/2
        i=0
        for i in range(len(X)):         #replace all the "NaN"s with it's feature median
            if X[i][k] == 'NaN':
                X[i][k]=median
            i=i+1
        k=k+1
    # print(len(X))
    return X
#test
impute_missing(X1[0])

#2b
#Because mean can be largely influenced by abnormal values
#such as really big or really small values, but median eliminates the influence of those abnormal values.

#2c   
def discard_missing(X,y):
    # print(X)
    k=0                     #initial settings
    NaN_recorder=[]
    new_X=[]
    new_y=[]
    l=0
    # print(len(y))
    for k in range (len(X)):   
        # print(len(X))
        i=0
        for i in range (279):   
            if X[k][i] == "NaN":             #record the position of the group of that "NaN" occurs
                NaN_recorder.append(k)
                break
            i=i+1
        k=k+1
    for l in range (len(X)):
        if l not in  NaN_recorder:              #copy the attribute groups that's not in the NaN_recorder list 
            new_X.append(X[l])    #those groups does not contain "NaN"
            new_y.append(y[l])
        l=l+1
    # print(len(new_X))
    X=new_X
    # print(len(X))
    y=new_y
    # print(X)
    # print(len(y))
    return X,y
#test 
discard_missing(X1[0],X1[1])