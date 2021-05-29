import numpy as np 

def function(x):

	r5 = 7
	r0 = 5
	paths = []
	try:
		if x >= 9:
			r5 = r5-5
			r0 = x/r0
			x = r0/x
			paths.append(1)
		else:
			x = 2*x
			paths.append(2)
		if r0 <= 9:
			r0 = 2+r0
			paths.append(3)
		else:
			r0 = r0/r0
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))