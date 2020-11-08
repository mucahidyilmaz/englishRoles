def iterative_ruler(cetvelUzunlugu, enUzunBölüt ):
    tmpenUzunBölüt = enUzunBölüt

    rulerIterator=1
    for i in range(0,cetvelUzunlugu):
        for j in range(0,pow(2,enUzunBölüt-3)):
            x= j+1/2
            if(j==0 and i==0):
                line = '-' * tmpenUzunBölüt 
                print(line + str(j))
            elif(int(x)%2==1 ):
                print('-')
                print('--')
                print('-')
                print('---')
            elif(int(x)%2==0 and j!=0):
                print('-')
                print('--')
                print('-')
                line = '-' * (tmpenUzunBölüt - 1 )
                print(line)git
        print('-')
        print('--')
        print('-')
        line = '-' * enUzunBölüt 
        print(line + str(rulerIterator))
        rulerIterator+=1

    
if __name__ == '__main__':
    iterative_ruler(1,5)
