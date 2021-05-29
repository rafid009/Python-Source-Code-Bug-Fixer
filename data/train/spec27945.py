import numpy as np 

def function(x):

	a8 = x
	v4 = x
	paths = []
	try:
		if v4 >= 2:
			a8 = a8/3
			x = 9*8
			a8 = a8-9
			paths.append(1)
		else:
			v4 = 6*v4
			x = x-8
			paths.append(2)
		if v4 <= 8:
			x = 9-v4
			paths.append(3)
		else:
			a8 = 1*a8
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		a8 = v4**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))