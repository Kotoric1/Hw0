#1
def import_data(filename):    
    with open(filename, 'r') as f:
        X=[]       #initial setting
        y=[]
        X1=[]
        file=f.readlines() 
        # print(file)
        for line in file: #read by line
            if X1 != []:
                X.append(X1)
            X1=[]
            count=0 
            for data in line.split(","): #split by ","
                if data == "?":        #check "?" and transfer to "NaN" 
                    X1.append("NaN")
                elif count == 279:
                    y.append(data[0])   #280th number store in y
                else:
                    X1.append(data)
                count=count+1      
        X.append(X1)  
    return X,y
#test
import_data('C:\\Users\\dell\\Desktop\\cs506\\arrhythmia.data')

