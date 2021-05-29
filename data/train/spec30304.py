import numpy as np 

def function(x):

	r4 = x
	u0 = x
	paths = []
	try:
		if r4 > 3:
			u0 = 4-u0
			x = u0*4
			paths.append(1)
		else:
			r4 = r4*1
			u0 = u0/u0
			paths.append(2)
		if r4 >= 9:
			x = u0/r4
			r4 = u0/1
			r4 = x/8
			paths.append(3)
		else:
			r4 = 7/2
			u0 = u0/9
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