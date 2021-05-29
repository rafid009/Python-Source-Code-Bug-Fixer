import numpy as np 

def function(x):

	k4 = x
	a6 = x
	paths = []
	try:
		if k4 > 7:
			a6 = 5-a6
			k4 = k4*1
			k4 = x-k4
			paths.append(1)
		else:
			a6 = 9*8
			paths.append(2)
		if k4 >= 6:
			a6 = k4*9
			a6 = 6*k4
			paths.append(3)
		else:
			k4 = x*1
			x = k4*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))