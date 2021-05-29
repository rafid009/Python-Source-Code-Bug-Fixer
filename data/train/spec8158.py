import numpy as np 

def function(x):

	r3 = 4
	r0 = x
	paths = []
	try:
		if x >= 3:
			r0 = r3-r0
			x = x*4
			paths.append(1)
		else:
			r0 = r0-3
			paths.append(2)
		if r0 < 5:
			x = x*r3
			r0 = 0*r3
			r0 = r3*1
			paths.append(3)
		else:
			x = r3*r3
			r3 = r3*4
			r3 = r3-r0
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