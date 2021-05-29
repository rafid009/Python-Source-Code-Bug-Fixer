import numpy as np 

def function(x):

	w8 = 2
	a9 = x
	paths = []
	try:
		if w8 < 2:
			x = x*w8
			paths.append(1)
		else:
			x = x+5
			x = a9-8
			paths.append(2)
		if x < 7:
			w8 = 1+6
			x = w8/a9
			a9 = 2+1
			paths.append(3)
		else:
			a9 = a9*4
			a9 = x*a9
			a9 = a9-2
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