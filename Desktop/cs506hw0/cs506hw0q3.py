import cs506hw0q2
import cs506hw0q1
X1=cs506hw0q1.import_data('C:\\Users\\dell\\Desktop\\cs506\\arrhythmia.data')   #import data set from question 1
X2=cs506hw0q2.discard_missing(X1[0],X1[1])                          #import discard_missing function in question 2c
                                                                    #for question 3, use the data returned from the discard_missing function
#3a
import random
def shuffle_data(X,y):
    random_number = random.randint(0,len(y)-1)      #set the same random seed in order to shuffle the random row of X 
    random.seed(random_number)                      #and it's corresponding y in the same random way
    random.shuffle(X)
    random.seed(random_number)
    random.shuffle(y)
    # print(X)
    return X,y
#test
shuffle_data(X2[0],X2[1])


# 3b
def calculate_mean(X):                  #build a helper function for calculating the mean which can be used in further functions
    mean_list=[]
    i=0
    for i in range(279):
        sum=0
        j=0
        for j in range(len(X)):         #calculate the mean and store them in a list
            sum=sum+float(X[j][i])
            j=j+1
        mean=sum/len(X)
        mean_list.append(mean)
        i=i+1
    return mean_list

def compute_std(X):
    mean=calculate_mean(X)              #call the mean list that we calculate above
    std=[]
    i=0
    for i in range(279):
        sum=0
        j=0
        for j in range(len(X)):                     #find the standard deviation
            sum=sum+(float(X[j][i])-mean[i])**2
            j=j+1
        standard_deviation=(sum/(len(X)-1))**0.5
        std.append(standard_deviation)
        i=i+1
    return std
compute_std(X2[0])


#3c
def remove_outlier(X,y):
    # print(len(X[0]))
    std=compute_std(X)                  #import previous functions for standard deviation and mean 
    mean=calculate_mean(X)
    outlier_list=[]
    new_X=[]
    new_y=[]
    i=0
    for i in range(len(X)):
        k=0
        for k in range(279):        #record the features that contains outlier
            if (float(X[i][k])<mean[k]-2*std[k]) or (float(X[i][k])>mean[k]+2*std[k]):
                outlier_list.append(i)
                break   
            else:            
                k=k+1  
            # print(k)     
        i=i+1
    # print(outlier_list)
    l=0
    for l in range (len(X)):
        if l not in  outlier_list:              #copy the features that's not in the outlier_list list 
            new_X.append(X[l])                  #those groups does not contain outliers
            new_y.append(y[l])   
        l=l+1 
    X=new_X
    y=new_y
    # print(X)
    # print(y)
    return X,y
# test
remove_outlier(X2[0],X2[1])
      

#3d
def standardize_data(X):
    # print(X)
    std=compute_std(X)      #get the standard deviation list from computer_std()
    # print(std)
    i=0
    for i in range(len(X)):
        sum1=0
        j=0
        for j in range(len(X[i])):            #calculate the mean of each feature
            sum1=sum1+float(X[i][j])
            j=j+1
        mean=sum1/len(X[i])
        k=0
        for k in range(len(X[i])):                  #change each x into standardized data x'
            if std[i] !=0:
                X[i][k]=(float(X[i][k])-mean)/(std[i])
            k=k+1
        i=i+1
    # print(X)
    return X
#testing
standardize_data(X2[0])

#Time complexity: n
#Space complexity: n
