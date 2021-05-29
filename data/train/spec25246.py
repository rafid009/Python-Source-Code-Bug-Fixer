import numpy as np 

def function(x):

	k2 = 0
	t8 = x
	paths = []
	try:
		if x < 0:
			k2 = x/4
			k2 = k2-6
			k2 = 6*3
			paths.append(1)
		else:
			k2 = k2-k2
			k2 = 2+3
			paths.append(2)
		if x < 4:
			x = x/2
			paths.append(3)
		else:
			k2 = 6*t8
			x = t8+9
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