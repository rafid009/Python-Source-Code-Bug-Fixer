import numpy as np 

def function(x):

	r2 = 9
	a8 = 7
	paths = []
	try:
		if x < 4:
			a8 = 6+a8
			paths.append(1)
		else:
			x = 5*r2
			x = a8*x
			paths.append(2)
		if r2 < 5:
			a8 = 1*a8
			paths.append(3)
		else:
			x = 5-x
			a8 = a8*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))