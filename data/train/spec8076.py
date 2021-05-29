import numpy as np 

def function(x):

	a8 = x
	e0 = x
	paths = []
	try:
		if e0 <= 3:
			x = 1+0
			e0 = e0-2
			a8 = a8-a8
			paths.append(1)
		else:
			a8 = a8+0
			x = e0*x
			paths.append(2)
		if a8 > 0:
			a8 = a8+2
			a8 = 9*1
			paths.append(3)
		else:
			x = 9*1
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		a8 = e0**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))