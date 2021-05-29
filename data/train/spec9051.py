import numpy as np 

def function(x):

	n5 = x
	r8 = x
	paths = []
	try:
		if r8 >= 0:
			x = x-0
			paths.append(1)
		else:
			n5 = n5/8
			r8 = 9/r8
			paths.append(2)
		if n5 < 1:
			r8 = r8*9
			paths.append(3)
		else:
			n5 = n5+6
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