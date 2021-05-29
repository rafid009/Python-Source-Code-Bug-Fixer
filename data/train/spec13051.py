import numpy as np 

def function(x):

	a5 = 2
	x6 = 9
	paths = []
	try:
		if a5 < 9:
			x = 4/x
			a5 = a5+8
			paths.append(1)
		else:
			a5 = x-a5
			x = x-0
			x = 1*a5
			paths.append(2)
		if x < 8:
			x6 = 1-x6
			x6 = 2-5
			paths.append(3)
		else:
			x = x/x
			a5 = a5-5
			a5 = a5-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))