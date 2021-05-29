import numpy as np 

def function(x):

	a3 = 5
	b4 = 2
	paths = []
	try:
		if a3 < 4:
			b4 = x*3
			a3 = 7/a3
			paths.append(1)
		else:
			x = x-4
			a3 = a3/7
			a3 = 3-a3
			paths.append(2)
		if x >= 2:
			a3 = 0-a3
			b4 = 4+b4
			paths.append(3)
		else:
			b4 = 8+b4
			a3 = 6*x
			b4 = 4/9
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