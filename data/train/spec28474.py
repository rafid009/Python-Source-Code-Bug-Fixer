import numpy as np 

def function(x):

	r0 = x
	r5 = 3
	paths = []
	try:
		if x < 6:
			x = r5/7
			r0 = 1-8
			paths.append(1)
		else:
			r5 = r0-3
			r0 = 3*r0
			r5 = r0+r5
			paths.append(2)
		if r0 >= 6:
			r5 = r5*r5
			x = x-9
			r0 = r0+6
			paths.append(3)
		else:
			r0 = 2-7
			x = r5*x
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