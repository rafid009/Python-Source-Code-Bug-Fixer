import numpy as np 

def function(x):

	r3 = 7
	n0 = 0
	paths = []
	try:
		if n0 <= 0:
			r3 = x/r3
			r3 = r3-r3
			paths.append(1)
		else:
			r3 = 9-r3
			paths.append(2)
		if r3 >= 4:
			r3 = 1-x
			x = x/2
			paths.append(3)
		else:
			n0 = 8+6
			r3 = r3+r3
			x = x/n0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))