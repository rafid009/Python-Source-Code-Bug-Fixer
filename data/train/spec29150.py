import numpy as np 

def function(x):

	a9 = x
	w8 = x
	paths = []
	try:
		if w8 >= 4:
			w8 = w8-4
			x = x/x
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if w8 >= 2:
			w8 = a9-w8
			a9 = 0-8
			paths.append(3)
		else:
			a9 = a9-a9
			x = a9/x
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		x = w8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))