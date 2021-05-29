import numpy as np 

def function(x):

	i0 = 8
	u0 = 6
	paths = []
	try:
		if i0 <= 2:
			i0 = x-u0
			i0 = 4*i0
			u0 = 9*u0
			paths.append(1)
		else:
			u0 = 5-u0
			paths.append(2)
		if i0 > 3:
			u0 = i0*u0
			u0 = 4/u0
			paths.append(3)
		else:
			i0 = 7+u0
			x = i0+6
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		i0 = u0**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))