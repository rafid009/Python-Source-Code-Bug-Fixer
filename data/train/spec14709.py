import numpy as np 

def function(x):

	a5 = 8
	x3 = 5
	paths = []
	try:
		if x3 <= 7:
			a5 = x3*a5
			x3 = x3+1
			x3 = x3/5
			paths.append(1)
		else:
			x = x-2
			x3 = 9*x3
			x3 = x3+x3
			paths.append(2)
		if a5 < 3:
			x3 = 0+x3
			paths.append(3)
		else:
			x3 = 0/4
			a5 = 7*a5
			x3 = 2/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))