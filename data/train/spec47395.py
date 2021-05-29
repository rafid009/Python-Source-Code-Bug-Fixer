import numpy as np 

def function(x):

	r0 = 8
	j4 = 0
	paths = []
	try:
		if x > 0:
			x = 8+r0
			r0 = r0-j4
			j4 = x+j4
			paths.append(1)
		else:
			j4 = 7*r0
			x = x+0
			j4 = 0*r0
			paths.append(2)
		if x <= 9:
			r0 = 4+4
			j4 = 1-3
			paths.append(3)
		else:
			x = 7/8
			j4 = j4*5
			r0 = 7-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))