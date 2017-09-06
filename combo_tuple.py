# If you have 2 list like this
# x = (1,2,3) and y = ('a','b','c')
# And you want to combine both of the tuples to this --> (1,'a',2,'b',3,'c')
# Use below

def combo(x,y):
  tuple_list= []
  for idx in range(len(x)):
    tuple_list.append((x[idx],y[idx]))
  return tuple_list
