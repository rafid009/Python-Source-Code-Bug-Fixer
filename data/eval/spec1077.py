import numpy as np 

def function(x):

	z4 = 4
	r0 = x
	paths = []
	try:
		if z4 >= 3:
			z4 = 5/9
			x = 4+x
			paths.append(1)
		else:
			x = 1*x
			x = z4/r0
			x = x/2
			paths.append(2)
		if x > 6:
			x = r0*z4
			x = 4+8
			paths.append(3)
		else:
			x = 5-x
			r0 = r0-r0
			r0 = 0*1
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