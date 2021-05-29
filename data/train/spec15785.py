import numpy as np 

def function(x):

	k4 = 1
	e0 = x
	paths = []
	try:
		if x > 4:
			e0 = e0*x
			e0 = x/k4
			paths.append(1)
		else:
			x = x-x
			x = e0/k4
			e0 = 8*x
			paths.append(2)
		if e0 >= 1:
			e0 = 3*e0
			paths.append(3)
		else:
			e0 = 3*9
			k4 = k4*1
			x = x*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))