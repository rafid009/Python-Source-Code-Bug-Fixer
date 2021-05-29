import numpy as np 

def function(x):

	e0 = 2
	j9 = 1
	paths = []
	try:
		if x <= 7:
			j9 = 3/x
			x = x/e0
			paths.append(1)
		else:
			j9 = x+6
			e0 = j9-8
			paths.append(2)
		if e0 >= 2:
			j9 = j9*e0
			x = j9*e0
			j9 = x+j9
			paths.append(3)
		else:
			j9 = j9/e0
			j9 = j9-0
			e0 = e0*x
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