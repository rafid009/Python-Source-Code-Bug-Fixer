import numpy as np 

def function(x):

	o4 = x
	u4 = x
	paths = []
	try:
		if o4 >= 3:
			o4 = 8*o4
			paths.append(1)
		else:
			u4 = u4-u4
			x = 3/x
			paths.append(2)
		if u4 > 8:
			x = x-2
			paths.append(3)
		else:
			u4 = u4+u4
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