import numpy as np 

def function(x):

	w8 = x
	a0 = 3
	paths = []
	try:
		if x >= 0:
			x = 6*6
			paths.append(1)
		else:
			w8 = 6*3
			w8 = 2-w8
			x = 3-x
			paths.append(2)
		if a0 >= 7:
			a0 = a0*7
			w8 = 5/a0
			paths.append(3)
		else:
			a0 = 3+a0
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		a0 = w8**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))