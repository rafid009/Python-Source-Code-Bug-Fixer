import numpy as np 

def function(x):

	u4 = x
	w6 = x
	paths = []
	try:
		if x >= 1:
			x = x+3
			paths.append(1)
		else:
			w6 = u4-w6
			paths.append(2)
		if w6 < 0:
			x = x-6
			paths.append(3)
		else:
			w6 = 3/u4
			u4 = u4+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))