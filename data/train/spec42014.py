import numpy as np 

def function(x):

	x7 = 6
	r8 = 0
	paths = []
	try:
		if r8 > 9:
			r8 = r8-r8
			paths.append(1)
		else:
			x7 = 4-0
			x7 = x7*6
			paths.append(2)
		if x >= 3:
			x7 = x7-6
			x = x7/3
			x = x*6
			paths.append(3)
		else:
			x = x-9
			r8 = x-0
			r8 = x7-0
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