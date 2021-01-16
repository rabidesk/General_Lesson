max = 20
list_1 = [''*(max-n-1)+'*'*(2*n+1) for n in range(max)]
list_2 = [''*int((2*max-int((2*max+1)*3/11))/2)+'*'*(int((2*max+1)*3/11)) for n in range(max//2)]

for top in list_1:
    print(top)

for tel in list_2:
    print(tel)

