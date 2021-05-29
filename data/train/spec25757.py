import numpy as np 

def function(x):

	a4 = x
	c2 = 8
	paths = []
	try:
		if a4 <= 7:
			x = x-3
			x = 0*1
			x = x-x
			paths.append(1)
		else:
			c2 = c2+4
			paths.append(2)
		if x <= 6:
			a4 = a4+1
			paths.append(3)
		else:
			x = c2*a4
			a4 = 3/c2
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))