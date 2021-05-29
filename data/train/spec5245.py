import numpy as np 

def function(x):

	b4 = 7
	i0 = x
	paths = []
	try:
		if x > 7:
			x = x-7
			i0 = 2-b4
			b4 = b4/i0
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if x >= 9:
			x = i0*x
			paths.append(3)
		else:
			b4 = b4*x
			i0 = i0-0
			i0 = 3*i0
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))