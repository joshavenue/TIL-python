y = ['something is inside here']

def removing():
  x = input('What do you want to remove?')
  
  try:
      y.remove(x)                     // remove(x) removes whatever you want to remove from the list
  except ValueError:
      print('It is invalid!')
  else:
      pass
      
    
