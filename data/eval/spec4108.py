import numpy as np 

def function(x):

	u4 = 3
	w6 = x
	paths = []
	try:
		if u4 >= 6:
			w6 = w6-3
			paths.append(1)
		else:
			u4 = 3-u4
			w6 = 9*w6
			paths.append(2)
		if x < 3:
			w6 = 0/4
			paths.append(3)
		else:
			u4 = 2*1
			w6 = 3-w6
			x = x*6
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