import numpy as np 

def function(x):

	n3 = 6
	b0 = 4
	paths = []
	try:
		if x >= 4:
			n3 = b0*6
			n3 = 9+n3
			paths.append(1)
		else:
			b0 = x*4
			b0 = 8*x
			x = b0/4
			paths.append(2)
		if n3 > 6:
			n3 = 4*b0
			n3 = 5*3
			paths.append(3)
		else:
			b0 = 0-3
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		n3 = b0**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))