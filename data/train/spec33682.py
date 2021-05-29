import numpy as np 

def function(x):

	a3 = 8
	x6 = 8
	paths = []
	try:
		if x < 3:
			x = x*7
			paths.append(1)
		else:
			x = 2/1
			paths.append(2)
		if x6 <= 2:
			x = 5-6
			a3 = 3-2
			paths.append(3)
		else:
			a3 = x*a3
			a3 = 5/x6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))