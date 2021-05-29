import numpy as np 

def function(x):

	n4 = x
	r3 = 7
	paths = []
	try:
		if n4 >= 1:
			x = n4-8
			r3 = 8*8
			r3 = r3*r3
			paths.append(1)
		else:
			r3 = x-2
			r3 = 4+x
			x = x-8
			paths.append(2)
		if r3 < 0:
			r3 = 9/2
			paths.append(3)
		else:
			n4 = n4*n4
			n4 = x-4
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