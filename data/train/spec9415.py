import numpy as np 

def function(x):

	r1 = 6
	r0 = 0
	paths = []
	try:
		if r0 > 9:
			r1 = r1+4
			r1 = 4+r1
			r1 = r1+6
			paths.append(1)
		else:
			r0 = 8-r0
			r0 = x-3
			r0 = x+r0
			paths.append(2)
		if r1 > 4:
			r0 = 8*r1
			r1 = r1-x
			x = x+3
			paths.append(3)
		else:
			r1 = x-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))