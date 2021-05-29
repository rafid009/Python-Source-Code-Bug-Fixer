import numpy as np 

def function(x):

	x2 = x
	v0 = 3
	paths = []
	try:
		if x2 >= 3:
			x = 7*1
			x2 = x2-x2
			paths.append(1)
		else:
			v0 = 1-3
			paths.append(2)
		if x >= 8:
			v0 = 5*3
			x2 = 7*x2
			x = x+5
			paths.append(3)
		else:
			x2 = x*5
			x2 = x2*x2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))