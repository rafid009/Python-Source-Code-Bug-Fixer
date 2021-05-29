import numpy as np 

def function(x):

	x5 = 1
	a4 = 8
	paths = []
	try:
		if a4 < 0:
			x5 = x-x5
			a4 = 3*a4
			paths.append(1)
		else:
			a4 = x+a4
			paths.append(2)
		if x < 4:
			x5 = x/x5
			x = 1*1
			paths.append(3)
		else:
			a4 = a4-x5
			x = a4*x
			x5 = 4/x5
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))