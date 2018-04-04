def flupp(message=None,count=1):
    i = 0
    while i < count:
        print(message)
        i+=1

m = input('message: ')
c = int(input('count: '))

flupp(m, c)
