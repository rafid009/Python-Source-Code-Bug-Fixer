import numpy as np 

def function(x):

	a7 = 7
	b9 = 3
	paths = []
	try:
		if a7 <= 8:
			b9 = b9/4
			a7 = a7/a7
			paths.append(1)
		else:
			a7 = 1-a7
			paths.append(2)
		if a7 > 8:
			a7 = b9-4
			paths.append(3)
		else:
			a7 = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))