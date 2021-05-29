import numpy as np 

def function(x):

	u4 = 2
	a5 = 0
	paths = []
	try:
		if x <= 9:
			a5 = a5*x
			a5 = 2-3
			paths.append(1)
		else:
			a5 = a5-x
			a5 = a5-1
			paths.append(2)
		if a5 >= 4:
			a5 = a5+a5
			paths.append(3)
		else:
			a5 = 3*a5
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