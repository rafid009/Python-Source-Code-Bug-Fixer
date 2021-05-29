import numpy as np 

def function(x):

	a3 = x
	n1 = 1
	x = x
	paths = []
	try:
		if x < 7:
			n1 = 3*n1
			n1 = 9+n1
			paths.append(1)
		else:
			a3 = 7-8
			n1 = n1+x
			x = x/2
			paths.append(2)
		if a3 <= 0:
			x = x*a3
			n1 = x-0
			paths.append(3)
		else:
			a3 = n1*3
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