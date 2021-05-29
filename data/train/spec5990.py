import numpy as np 

def function(x):

	f7 = x
	x0 = 5
	paths = []
	try:
		if x >= 6:
			x0 = x0/4
			x = x/3
			f7 = f7/x0
			paths.append(1)
		else:
			x = x*x0
			paths.append(2)
		if f7 < 4:
			f7 = f7*x
			x0 = 2*x0
			paths.append(3)
		else:
			x0 = x-1
			f7 = 3*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))