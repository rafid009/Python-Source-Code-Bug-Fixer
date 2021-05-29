import numpy as np 

def function(x):

	o9 = 7
	a9 = x
	paths = []
	try:
		if a9 <= 3:
			x = x/o9
			a9 = a9+x
			paths.append(1)
		else:
			a9 = a9*4
			x = x-1
			paths.append(2)
		if x >= 3:
			o9 = x-3
			paths.append(3)
		else:
			x = x*7
			o9 = x-o9
			x = x+6
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