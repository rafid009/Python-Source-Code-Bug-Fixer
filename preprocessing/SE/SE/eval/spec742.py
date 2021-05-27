import numpy as np 

def function(x):

	r0 = 8
	y7 = x
	paths = []
	try:
		if x >= 3:
			r0 = x+5
			paths.append(1)
		else:
			x = 9*x
			x = x+5
			r0 = 4/2
			paths.append(2)
		if x >= 3:
			r0 = r0*8
			x = r0*x
			paths.append(3)
		else:
			y7 = 5-y7
			r0 = 8+r0
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))