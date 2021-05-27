import numpy as np 

def function(x):

	y2 = 6
	r0 = x
	paths = []
	try:
		if x <= 8:
			x = x-8
			paths.append(1)
		else:
			y2 = y2/r0
			x = y2*x
			r0 = r0*2
			paths.append(2)
		if r0 >= 3:
			x = x-3
			r0 = 1-y2
			x = r0-y2
			paths.append(3)
		else:
			x = 9-0
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		x = r0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))