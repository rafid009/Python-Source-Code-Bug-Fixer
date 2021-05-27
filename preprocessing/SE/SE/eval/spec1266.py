import numpy as np 

def function(x):

	i4 = 0
	k2 = x
	paths = []
	try:
		if i4 < 8:
			x = 1-6
			x = x-0
			i4 = 0+8
			paths.append(1)
		else:
			x = 3-x
			x = x+2
			paths.append(2)
		if k2 >= 9:
			i4 = i4/6
			paths.append(3)
		else:
			x = 5*i4
			i4 = i4*k2
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