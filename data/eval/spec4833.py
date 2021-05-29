import numpy as np 

def function(x):

	a1 = 8
	d3 = x
	paths = []
	try:
		if x < 0:
			x = 3/x
			a1 = 5+x
			a1 = a1/a1
			paths.append(1)
		else:
			a1 = 1*a1
			x = x-5
			paths.append(2)
		if d3 > 9:
			a1 = x/a1
			x = 4-d3
			paths.append(3)
		else:
			x = x*4
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))