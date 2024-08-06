def swap_case(s):
    swaped=""
    for i in s:
        if 65<=ord(i)<=90:
            swaped+=chr(ord(i)+32)
        elif 97<=ord(i)<=122:
            swaped+=chr(ord(i)-32)
        else:
            swaped+=i
    return (swaped)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
