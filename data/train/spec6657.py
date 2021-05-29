import numpy as np 

def function(x):

	i9 = 3
	w4 = x
	paths = []
	try:
		if w4 <= 8:
			w4 = w4+0
			paths.append(1)
		else:
			i9 = 8-i9
			x = w4*x
			paths.append(2)
		if i9 >= 2:
			w4 = w4-0
			w4 = w4-4
			paths.append(3)
		else:
			x = 4-x
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