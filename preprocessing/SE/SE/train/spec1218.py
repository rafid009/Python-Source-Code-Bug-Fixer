import numpy as np 

def function(x):

	w4 = x
	b4 = 4
	paths = []
	try:
		if x > 2:
			w4 = 7/9
			paths.append(1)
		else:
			x = b4/x
			x = x-5
			paths.append(2)
		if w4 > 0:
			x = x+7
			paths.append(3)
		else:
			x = 9-b4
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))