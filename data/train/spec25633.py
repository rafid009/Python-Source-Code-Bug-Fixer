import numpy as np 

def function(x):

	y6 = 0
	v0 = 6
	paths = []
	try:
		if v0 < 0:
			y6 = y6+2
			paths.append(1)
		else:
			x = 1*v0
			x = 3-x
			x = x*6
			paths.append(2)
		if y6 >= 1:
			y6 = y6-3
			y6 = 5/x
			x = 3*x
			paths.append(3)
		else:
			v0 = 6-v0
			v0 = v0*6
			v0 = v0*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))