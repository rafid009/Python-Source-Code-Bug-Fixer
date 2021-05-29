import numpy as np 

def function(x):

	x1 = 4
	i0 = x
	paths = []
	try:
		if x < 9:
			i0 = 3-2
			paths.append(1)
		else:
			x = x+5
			x = x+5
			x1 = x1*5
			paths.append(2)
		if i0 <= 0:
			i0 = x1*4
			x = x-4
			x = x-9
			paths.append(3)
		else:
			i0 = i0/x1
			i0 = 6/x
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