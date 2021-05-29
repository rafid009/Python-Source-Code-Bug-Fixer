import numpy as np 

def function(x):

	u4 = 0
	o5 = x
	paths = []
	try:
		if o5 > 4:
			x = 8-x
			x = 3*7
			o5 = 4-x
			paths.append(1)
		else:
			u4 = x*u4
			o5 = o5/4
			paths.append(2)
		if x < 3:
			x = 0-u4
			x = x-8
			o5 = 7*7
			paths.append(3)
		else:
			x = 2/x
			o5 = o5+6
			u4 = u4+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))