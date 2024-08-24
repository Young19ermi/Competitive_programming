if __name__ == '__main__':
    N = int(input())
    mylist=[]
    for _ in range(N):
        command=input()
        if command[:3]=="ins":
            i=int(command[7:(command[7:].index(" ")+7)])
            e=command[9:]
            mylist.insert(i,int(e))
        elif command[:3]=="rem":
            e=command[7:]
            mylist.remove(int(e))
        elif command[:3]=="app":
            e=command[7:]
            mylist.append(int(e))
        elif command=='print':
            print(mylist)
        elif command=="pop":
            mylist.pop()
        elif command=="sort":
            mylist.sort()
        elif command=="reverse":
            mylist.reverse()
    
