import numpy as np 

def function(x):

	x0 = x
	r0 = x
	paths = []
	try:
		if x0 > 2:
			x0 = x0*x
			x = x-7
			paths.append(1)
		else:
			r0 = 6-r0
			x0 = 4+1
			paths.append(2)
		if r0 >= 8:
			r0 = r0*0
			x0 = x0-8
			paths.append(3)
		else:
			x0 = x0*6
			r0 = r0*5
			r0 = r0-r0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))