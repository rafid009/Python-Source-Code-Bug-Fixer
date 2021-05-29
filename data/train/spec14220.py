import numpy as np 

def function(x):

	r6 = 6
	c2 = 0
	paths = []
	try:
		if c2 <= 4:
			r6 = 7+9
			paths.append(1)
		else:
			r6 = r6*r6
			x = 0-4
			x = 0*x
			paths.append(2)
		if x < 7:
			r6 = 5*r6
			x = x-2
			paths.append(3)
		else:
			x = 4*r6
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