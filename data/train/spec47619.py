import numpy as np 

def function(x):

	n0 = x
	a4 = x
	x = 6
	paths = []
	try:
		if x < 7:
			x = n0+0
			a4 = 3+a4
			n0 = 5*n0
			paths.append(1)
		else:
			n0 = n0*9
			n0 = 5*n0
			n0 = 6-1
			paths.append(2)
		if n0 > 3:
			a4 = 6/3
			a4 = a4-4
			n0 = n0/9
			paths.append(3)
		else:
			a4 = a4*a4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))