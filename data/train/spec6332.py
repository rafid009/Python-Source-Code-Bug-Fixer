import numpy as np 

def function(x):

	a9 = x
	w5 = x
	x = x
	paths = []
	try:
		if x > 3:
			a9 = a9+0
			paths.append(1)
		else:
			a9 = 5/a9
			paths.append(2)
		if a9 >= 9:
			x = x*7
			a9 = 1+a9
			x = 1-x
			paths.append(3)
		else:
			x = 9+x
			x = x*7
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