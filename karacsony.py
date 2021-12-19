import os



x = int(input('December hanyadika van ma?: '))
x =int(x)
print(24-x,'nap van karácsonyig.')




if (12 < x < 24):
    print('3 gyertya ég')
    print(r"""
    
   ___)__    ___)__
  |      |  |      |
  |      |  |      |
  |      |  |      |
  |      |  |      |
  '------'  '------'
           ___)__
          |      |
          |      |
          |      |
          |      |
          '------' 
    
    """)
if (0 < x < 5):
    print('1 gyertya ég ')
    print(r"""
  
           ___)__
          l      l
          l      l
          l      l
          l      l
          '------' 
 """)
if (5 < x < 12):
    print("2 gyertya ég")
    print(r"""
   ___)__    ___)__
  |      |  |      |
  |      |  |      |
  |      |  |      |
  |      |  |      |
  '------'  '------'
""")
if  (24 < x):
    print("4 gyertya ég")
    print(r"""
        
   ___)__    ___)__
  |      |  |      |
  |      |  |      |
  |      |  |      |
  |      |  |      |
  '------'  '------'
   ___)__    ___)__
  |      |  |      |
  |      |  |      |
  |      |  |      |
  |      |  |      |
  '------'  '------'
        """)


