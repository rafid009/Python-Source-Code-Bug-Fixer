import numpy as np 

def function(x):

	a5 = x
	k1 = 7
	paths = []
	try:
		if a5 >= 4:
			x = 8/6
			paths.append(1)
		else:
			k1 = 2*9
			x = 3*x
			k1 = 4+1
			paths.append(2)
		if a5 > 0:
			x = 4-6
			a5 = a5*7
			paths.append(3)
		else:
			a5 = x/9
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