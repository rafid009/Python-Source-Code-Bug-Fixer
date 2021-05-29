import numpy as np 

def function(x):

	u4 = 2
	o8 = x
	paths = []
	try:
		if o8 >= 8:
			x = 6/x
			o8 = o8+6
			paths.append(1)
		else:
			o8 = 3-o8
			x = x/6
			paths.append(2)
		if x <= 0:
			o8 = o8/8
			paths.append(3)
		else:
			o8 = 0/4
			x = 4/3
			u4 = 9*u4
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