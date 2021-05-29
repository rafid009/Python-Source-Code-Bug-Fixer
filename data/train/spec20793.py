import numpy as np 

def function(x):

	v4 = 9
	a4 = 9
	x = x
	paths = []
	try:
		if x < 7:
			v4 = 7-v4
			paths.append(1)
		else:
			a4 = a4*8
			x = 4/9
			paths.append(2)
		if a4 > 2:
			x = x-5
			paths.append(3)
		else:
			v4 = v4-v4
			x = x-a4
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