import numpy as np 

def function(x):

	a4 = 8
	r0 = 5
	paths = []
	try:
		if x <= 2:
			r0 = a4*1
			paths.append(1)
		else:
			x = x*5
			x = r0+x
			x = 1/x
			paths.append(2)
		if r0 >= 5:
			r0 = 0/r0
			x = x+r0
			paths.append(3)
		else:
			r0 = r0*4
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