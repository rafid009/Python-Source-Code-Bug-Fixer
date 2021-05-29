import numpy as np 

def function(x):

	w9 = x
	a8 = x
	paths = []
	try:
		if a8 >= 2:
			w9 = 6+w9
			a8 = a8*1
			a8 = w9-4
			paths.append(1)
		else:
			w9 = w9+8
			x = 0-w9
			w9 = w9-x
			paths.append(2)
		if a8 >= 6:
			x = x-w9
			paths.append(3)
		else:
			a8 = x/a8
			x = x+1
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		a8 = w9**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))