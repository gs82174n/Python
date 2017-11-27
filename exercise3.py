print float(123)
print float('123')
print float('123.23')
print int(123.23)
#   File "exercise3.py", line 5, in <module>
#    print int('123.23')
#ValueError: invalid literal for int() with base 10: '123.23'
#above is an error given for the below line of code. I commented it off so the
#code would execute 
#print int('123.23')
print int(float('123.23'))
print str(12)
print str(12.2)
print bool('a')
print bool(0)
print bool(0.1)
