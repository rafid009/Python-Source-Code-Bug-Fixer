import numpy as np 

def function(x):

	r0 = 9
	l2 = 9
	paths = []
	try:
		if l2 < 2:
			x = 1-2
			r0 = r0+0
			r0 = 0*r0
			paths.append(1)
		else:
			r0 = 3*8
			paths.append(2)
		if x > 0:
			l2 = 9+3
			paths.append(3)
		else:
			r0 = r0+7
			l2 = 6-4
			r0 = 7*r0
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