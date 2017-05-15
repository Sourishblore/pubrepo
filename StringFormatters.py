'''
Created on May 7, 2017

@author: sourish.sarkar
'''
s1='apples'
s2="oranges"
s3="grapes"
s5="John likes {},{},{}".format(s1,s2,s3)
print("s5" ,s5)
#Positional arguments
s6="John likes {1},{0}, {1}".format(s1,s2)
print("s6:",s6)
#Keyword arguments
s7="John likes {app},{ora},{app}".format(app=s1.capitalize(),ora=s2.swapcase())
print("s7:",s7)
#Keyword and Positional arguments can be used together
s8="John likes {ora},{0}".format(s1,ora=s2)
print("s8:",s8)