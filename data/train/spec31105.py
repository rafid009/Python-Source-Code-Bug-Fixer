import numpy as np 

def function(x):

	x0 = 7
	f3 = x
	paths = []
	try:
		if f3 >= 0:
			x = x+8
			x0 = x0/2
			x0 = x0*x0
			paths.append(1)
		else:
			f3 = f3/7
			paths.append(2)
		if x <= 6:
			x = x+6
			paths.append(3)
		else:
			x = 5-x
			f3 = f3-f3
			x0 = f3*4
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