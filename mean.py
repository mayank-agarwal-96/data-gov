def mean(x):
    return float(sum(x))/len(x)

def variance(x):
    m = mean(x)
    sq = [(i-m)**2 for i in x]    
    return float(sum(sq))/len(x)
    
data = []
while 1:
    p = int(input("Enter data ( 0 to close) :"))
    if p == 0:
        break
    data.append(p)

print ("Mean of data :" ,mean(data))
print ("Variance of data :", variance(data))
