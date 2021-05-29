import numpy as np 

def function(x):

	i1 = x
	u9 = x
	paths = []
	try:
		if x < 0:
			i1 = 3+4
			i1 = 0*5
			i1 = 8*6
			paths.append(1)
		else:
			u9 = u9*x
			u9 = u9+u9
			paths.append(2)
		if i1 >= 0:
			x = x*6
			paths.append(3)
		else:
			u9 = 9/7
			u9 = 5*u9
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