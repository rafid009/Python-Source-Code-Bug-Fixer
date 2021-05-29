import numpy as np 

def function(x):

	a2 = 5
	k4 = 2
	paths = []
	try:
		if a2 > 9:
			x = x/5
			k4 = x/x
			paths.append(1)
		else:
			k4 = a2*k4
			x = k4+x
			a2 = 8+5
			paths.append(2)
		if a2 > 9:
			x = x*a2
			k4 = a2*k4
			paths.append(3)
		else:
			a2 = 9-8
			k4 = x-3
			k4 = k4/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))