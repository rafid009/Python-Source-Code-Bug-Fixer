import numpy as np 

def function(x):

	w4 = x
	i9 = 3
	paths = []
	try:
		if i9 <= 1:
			i9 = 5/5
			w4 = w4-x
			i9 = i9-5
			paths.append(1)
		else:
			i9 = i9-8
			paths.append(2)
		if i9 <= 5:
			w4 = 2/i9
			i9 = i9*i9
			x = 0-x
			paths.append(3)
		else:
			x = w4+x
			i9 = w4+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))