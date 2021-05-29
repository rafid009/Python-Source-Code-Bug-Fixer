import numpy as np 

def function(x):

	k5 = 3
	r0 = 9
	paths = []
	try:
		if r0 >= 1:
			k5 = k5/r0
			r0 = 6-3
			x = x-2
			paths.append(1)
		else:
			x = 9-k5
			k5 = k5+7
			r0 = x*r0
			paths.append(2)
		if x < 1:
			k5 = k5+3
			paths.append(3)
		else:
			k5 = 3*8
			r0 = r0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))