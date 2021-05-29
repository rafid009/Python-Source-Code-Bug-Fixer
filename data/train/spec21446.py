import numpy as np 

def function(x):

	x9 = 8
	r6 = 1
	paths = []
	try:
		if x < 1:
			r6 = 9-6
			paths.append(1)
		else:
			r6 = 3*r6
			r6 = r6/9
			paths.append(2)
		if x >= 3:
			x9 = 1+2
			r6 = r6/4
			r6 = 6-8
			paths.append(3)
		else:
			x9 = 6/x9
			x = x-7
			r6 = 2+r6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))