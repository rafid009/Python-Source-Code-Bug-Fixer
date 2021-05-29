import numpy as np 

def function(x):

	w9 = x
	a5 = x
	paths = []
	try:
		if x >= 8:
			x = x-x
			w9 = w9-9
			paths.append(1)
		else:
			a5 = a5/x
			w9 = 5/w9
			paths.append(2)
		if x > 5:
			x = x/4
			x = w9*3
			x = 1-x
			paths.append(3)
		else:
			x = 5-4
			w9 = w9+2
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		a5 = w9**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))