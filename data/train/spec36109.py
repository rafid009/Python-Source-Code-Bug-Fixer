import numpy as np 

def function(x):

	e0 = 6
	i6 = 5
	paths = []
	try:
		if x >= 9:
			e0 = 9+8
			paths.append(1)
		else:
			i6 = i6+2
			x = e0-e0
			x = 4-i6
			paths.append(2)
		if x <= 6:
			e0 = e0*5
			e0 = 6-e0
			e0 = e0/5
			paths.append(3)
		else:
			i6 = i6/9
			x = x+3
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