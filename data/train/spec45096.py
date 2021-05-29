import numpy as np 

def function(x):

	u9 = x
	v4 = 1
	paths = []
	try:
		if x >= 4:
			x = x-8
			u9 = u9/v4
			x = 0-x
			paths.append(1)
		else:
			v4 = v4-7
			paths.append(2)
		if v4 >= 2:
			v4 = v4-9
			x = x+3
			paths.append(3)
		else:
			u9 = u9*8
			u9 = 7*u9
			v4 = u9+v4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))