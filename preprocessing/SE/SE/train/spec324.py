import numpy as np 

def function(x):

	a9 = 9
	w8 = 8
	paths = []
	try:
		if x > 5:
			w8 = w8/1
			a9 = a9+9
			x = x*4
			paths.append(1)
		else:
			a9 = 5*a9
			a9 = 5+a9
			paths.append(2)
		if a9 < 1:
			a9 = 7/8
			a9 = x+9
			paths.append(3)
		else:
			w8 = 5+w8
			a9 = 9+a9
			w8 = w8-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))