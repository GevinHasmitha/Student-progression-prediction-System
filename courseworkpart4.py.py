prog=0
trail=0
excl=0
retr=0
pro=[]
trai=[]
retri=[]
exclu=[]

var4=0
while var4==0:
                      #part 1
    
    var1 = 0
    while var1 == 0:
        try:
            c_pass = int(input('please enter your credits at pass '))
        except:
            print('enter an integer')
            continue
        if c_pass == 0 or c_pass == 20 or c_pass == 40 or c_pass == 60 or c_pass == 80 or c_pass == 100 or c_pass == 120:
            break
        else:
            print('out of range')

    var2 = 1
    while var2 == 1:
        try:
            c_diff = int(input('please enter your credits at differ '))
        except:
            print('enter an integer')
            continue
        if c_diff == 0 or c_diff == 20 or c_diff == 40 or c_diff == 60 or c_diff == 80 or c_diff == 100 or c_diff == 120:
            break
        else:
            print('out of range')

    var3 = 1
    while var3 == 1:
        try:
            c_fail = int(input('please enter your credits at fail '))
        except:
            print('enter an integer')
            continue
        if c_fail == 0 or c_fail == 20 or c_fail == 40 or c_fail == 60 or c_fail == 80 or c_fail == 100 or c_fail == 120:
            break
        else:
            print('out of range')

    total = c_pass + c_diff + c_fail
    if total != 120:
        print('total incorrect')
        
    if c_diff == 0 and c_fail == 0:
        print('Progress')       
        pro.append([c_pass,c_diff,c_fail])
        prog=prog+1
        
    elif c_pass == 100 and (c_diff == 0 or c_diff == 20) and (c_fail == 0 or c_fail == 20):
        print('Progress (module trailer)')        
        trai.append([c_pass,c_diff,c_fail])
        trail=trail+1
        
    elif (c_pass == 40 and c_diff == 0 and c_fail == 80) or (c_pass == 20 and c_diff == 20 and c_fail == 80) or (
            c_pass == 20 and c_diff == 0 and c_fail == 100) or (c_pass == 0 and c_diff == 40 and c_fail == 80) or (
            c_pass == 0 and c_diff == 20 and c_fail == 100) or (c_pass == 0 and c_diff == 0 and c_fail == 120):
        print('Exclude')
        exclu.append([c_pass,c_diff,c_fail])
        excl=excl+1
        
    else:
        print('Do not progress – module retriever ')
        retri.append([c_pass,c_diff,c_fail])
        retr=retr+1

    response = input('\nWould you like to enter another set of data?\nEnter "y" for yes or "q"" to quit and view results\n')
    if response=='y' :
        continue
    elif response=='q' :
        break
    else:
        print('invalid option')

#part 4
file=open('part4file','w')
for i in range(prog):
    file.write('progress'+str(pro[i]) +'\n')
for i in range(trail):
    file.write('progress(module trailer)'+str(trai[i]) +'\n')
for i in range(retr):
    file.write('module retriever'+str(retri[i]) +'\n')
for i in range(excl):
    file.write('Exclude'+str(exclu[i]) +'\n')
file.close()
file=open('part4file','r')
content=file.read()
print(content)
file.close()



    
