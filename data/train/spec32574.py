import numpy as np 

def function(x):

	j4 = 0
	y0 = 6
	paths = []
	try:
		if j4 < 8:
			j4 = j4-j4
			paths.append(1)
		else:
			y0 = y0*5
			j4 = x+j4
			j4 = j4+y0
			paths.append(2)
		if j4 > 8:
			j4 = j4/5
			paths.append(3)
		else:
			x = j4-3
			j4 = 1/4
			j4 = j4*y0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))