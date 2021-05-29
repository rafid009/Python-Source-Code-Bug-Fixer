import numpy as np 

def function(x):

	x9 = x
	r0 = x
	paths = []
	try:
		if x9 >= 3:
			r0 = 2-0
			x9 = 1+x9
			x9 = 2*x9
			paths.append(1)
		else:
			x9 = r0-x9
			paths.append(2)
		if x9 < 5:
			x9 = x9-2
			paths.append(3)
		else:
			x9 = x9*6
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		r0 = x9**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))