import numpy as np 

def function(x):

	a0 = 6
	v5 = 8
	paths = []
	try:
		if v5 <= 7:
			x = x-1
			paths.append(1)
		else:
			a0 = v5-3
			paths.append(2)
		if a0 > 0:
			a0 = 2+a0
			paths.append(3)
		else:
			a0 = a0+a0
			v5 = v5*6
			v5 = x/v5
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