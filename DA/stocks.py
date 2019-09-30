import sys

def mean(list):
    list_sum = sum(list)
    mean = list_sum/len(list)
    return mean

def std(list):
    std = 0
    list_mean = mean(list)
    for i in range(len(list)):
        std += (list[i] - list_mean)**2
    std = (std)**0.5
    return std  

def corr(list1, list2):
    num = 0
    corr = 0
    list1_m = mean(list1)
    list2_m = mean(list2)

    for i in range(len(list1)):
        num += (list1[i] - list1_m)*(list2[i] - list2_m)
    den = std(list1)*std(list2)
    
    corr = round((num/den),3)

    return corr

def readclose(datafile):
    
    data = []

    f = open(datafile)
    l = f.readline()

    while(l != '') : #read
        a = l.split(",")
        b = len(a)
        
        for j in range(b):
            if j == 5:
                data.append((a[j]))
            else:
                continue

        l = f.readline()

    #pop the first element from the list
    first = data.pop(0)
    
    #convert items in list usinf list comprehension
    data = [float(item) for item in data]
    
    return data

#read input data for the following companies
# 'IBM', 'MSFT', 'GOOG', 'AAPL', 'AMZN', 'FB'
IBMdata = readclose('IBM.csv')
MSFTdata = readclose('MSFT.csv')
GOOGdata = readclose('GOOG.csv')
AAPLdata = readclose('AAPL.csv')
AMZNdata = readclose('AMZN.csv')
FBdata = readclose('FB.csv')

#createa a dictionary for all adj close prices
allprices = {}
allprices['IBM'] = IBMdata 
allprices['MSFT'] = MSFTdata
allprices['GOOG'] = GOOGdata
allprices['AAPL'] = AAPLdata
allprices['AMZN'] = AMZNdata
allprices['FB'] = FBdata

# print(allprices)

# 'IBM', 'MSFT', 'GOOG', 'AAPL', 'AMZN', 'FB'
correlations = {} # create a dictionary for storing correlations
correlations['IBM:MSFT'] = corr(allprices['IBM'],allprices['MSFT'])
correlations['IBM:GOOG'] = corr(allprices['IBM'],allprices['GOOG'])
correlations['IBM:AAPL'] = corr(allprices['IBM'],allprices['AAPL'])
correlations['IBM:AMZN'] = corr(allprices['IBM'],allprices['AMZN'])
correlations['IBM:FB'] = corr(allprices['IBM'],allprices['FB'])
correlations['MSFT:GOOG'] = corr(allprices['MSFT'],allprices['GOOG'])
correlations['MSFT:AAPL'] = corr(allprices['MSFT'],allprices['AAPL'])
correlations['MSFT:AMZN'] = corr(allprices['MSFT'],allprices['AMZN'])
correlations['MSFT:FB'] = corr(allprices['MSFT'],allprices['FB'])
correlations['GOOG:AAPL'] = corr(allprices['GOOG'],allprices['AAPL'])
correlations['GOOG:AMZN'] = corr(allprices['GOOG'],allprices['AMZN'])
correlations['GOOG:FB'] = corr(allprices['GOOG'],allprices['FB'])
correlations['AAPL:AMZN'] = corr(allprices['AAPL'],allprices['AMZN'])
correlations['AAPL:FB'] = corr(allprices['AAPL'],allprices['FB'])
correlations['AMZN:FB'] = corr(allprices['AMZN'],allprices['FB'])

correlations = dict(sorted(correlations.items(),key = lambda x : x[1],reverse = True))

# print(len(correlations))

for key,value in correlations.items():
    print(key,"=",value)




