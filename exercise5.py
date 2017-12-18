def main():
    num = 0
    x = 11
    while (num<20):
        if x/5 == 0 and x/7 == 0 and x/11 == 0:
            print 'X = ', x
            num = num + 1
        x = x + 1
print(main())
