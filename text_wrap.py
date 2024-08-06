import textwrap

def wrap(string, max_width):
    newstring=""
    for i in range(len(string)):
        if i!=0 and  i%max_width==0:
            newstring+="\n"
            newstring+=string[i]
        else:
            newstring+=string[i]
       
    return newstring


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
