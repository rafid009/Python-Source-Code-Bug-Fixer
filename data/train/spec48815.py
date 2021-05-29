import numpy as np 

def function(x):

	w9 = 3
	i6 = 9
	paths = []
	try:
		if i6 >= 5:
			w9 = w9+w9
			i6 = w9/w9
			w9 = w9-9
			paths.append(1)
		else:
			w9 = 6+7
			x = i6*7
			paths.append(2)
		if i6 >= 2:
			w9 = 1-w9
			paths.append(3)
		else:
			x = w9/x
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