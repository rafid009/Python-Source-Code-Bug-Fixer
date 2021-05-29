import numpy as np 

def function(x):

	x0 = x
	a5 = 2
	paths = []
	try:
		if x > 9:
			x = x/1
			paths.append(1)
		else:
			a5 = 1*a5
			x0 = x0/x0
			x = 1+x
			paths.append(2)
		if x < 3:
			x0 = x0/6
			x0 = x0+5
			paths.append(3)
		else:
			x0 = x0+7
			x0 = 7-a5
			x0 = x0-a5
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