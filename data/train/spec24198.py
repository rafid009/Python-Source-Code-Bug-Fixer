import numpy as np 

def function(x):

	z4 = 5
	r8 = x
	paths = []
	try:
		if r8 < 9:
			x = 8-x
			r8 = r8-4
			r8 = r8/1
			paths.append(1)
		else:
			x = x+2
			r8 = 6-r8
			x = 0-x
			paths.append(2)
		if z4 < 6:
			x = 7/5
			x = x-8
			paths.append(3)
		else:
			r8 = r8/1
			z4 = 9-0
			z4 = 0+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))