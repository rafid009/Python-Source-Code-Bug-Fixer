import numpy as np 

def function(x):

	q9 = x
	a8 = 6
	paths = []
	try:
		if x >= 5:
			a8 = a8*3
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if a8 <= 2:
			x = 2+0
			paths.append(3)
		else:
			q9 = q9+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))