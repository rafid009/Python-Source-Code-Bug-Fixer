import numpy as np 

def function(x):

	i4 = 8
	w8 = x
	paths = []
	try:
		if w8 >= 8:
			w8 = i4/w8
			i4 = i4-i4
			paths.append(1)
		else:
			i4 = i4/x
			paths.append(2)
		if i4 >= 6:
			x = w8+7
			i4 = i4+3
			paths.append(3)
		else:
			w8 = i4*w8
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