import numpy as np 

def function(x):

	x3 = x
	r4 = x
	paths = []
	try:
		if r4 >= 6:
			r4 = 6*r4
			x = 2+x
			x = x+0
			paths.append(1)
		else:
			x = x3-1
			paths.append(2)
		if x < 6:
			x = r4/x
			r4 = r4+8
			x = x3*7
			paths.append(3)
		else:
			x3 = x*x
			r4 = 6/r4
			r4 = r4*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))