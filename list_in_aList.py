a = [0,1,2,3,4,5,6,7,8,9]

print(a[5])
print(a[a[5]])

## First, when a[5], you will get 5 from the list, the you list again with a[5], you will get the same number

b = [1,1,2,3,5,8,13]

print(b[4])
print(b[b[4]])

## b[4] , you will get 5. Then, that number 5 goes into the b[5], you will get 8 instead now. Same as b[b[4]] == b[5]

c = [2,5,2,5,7,2,8,4,7,9]

print(c[5])
print(c[c[5]])

d = [1,1,4,6,9,12,113,1223]

print(d[3])
print(d[d[3]])
## The outcome is really strange...##
