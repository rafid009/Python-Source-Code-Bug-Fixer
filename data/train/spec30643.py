import numpy as np 

def function(x):

	v0 = 7
	u0 = x
	x = x
	paths = []
	try:
		if v0 >= 6:
			v0 = v0/9
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if x < 1:
			u0 = 4*u0
			paths.append(3)
		else:
			u0 = 5*u0
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