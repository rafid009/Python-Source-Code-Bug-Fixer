import numpy as np 

def function(x):

	k2 = x
	a3 = 8
	paths = []
	try:
		if k2 >= 3:
			x = 0/k2
			k2 = 9/6
			paths.append(1)
		else:
			k2 = 5/7
			paths.append(2)
		if k2 > 9:
			a3 = 9-9
			a3 = a3*a3
			paths.append(3)
		else:
			k2 = 2*5
			x = x*8
			a3 = k2*a3
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