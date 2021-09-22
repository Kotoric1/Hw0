def import_train_data(filename):
    with open(filename,'r') as file:        #read csv file
        f=file.readlines()
        X=[]
        y=[]
        X1=[]
        for line in f:
            line=line.strip('\n')           #delete "\n"
            line=line.strip(',')
            count=0
            if X1 != []:
                X.append(X1)
            X1=[]
            for data in line.split(","):        #split with ","
                if count == 1:                  #copy the "survived" to y
                    y.append(data)
                else:                           #copy other to X
                    if data == "male":
                        X1.append(1)
                    elif data == "female":      #change non-numerical values to numbers
                        X1.append(0)
                    elif data == "C":
                        X1.append(0)
                    elif data == "Q":
                        X1.append(1)
                    elif data == "S":
                        X1.append(2)
                        
                    else:
                        X1.append(data)
                count=count+1
        X.append(X1) 
    del X[0]         #delete the feature name line
    del y[0]  
    # print(X)
    # print(y)
    return X,y
#test
file="C:\\Users\\dell\\Desktop\\cs506\\hw\\train.csv"
import_train_data(file)