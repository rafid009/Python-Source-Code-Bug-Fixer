import numpy as np 

def function(x):

	v4 = 9
	j0 = 1
	paths = []
	try:
		if j0 > 3:
			x = x-2
			x = x*x
			v4 = v4-5
			paths.append(1)
		else:
			j0 = j0+3
			v4 = v4-x
			paths.append(2)
		if v4 > 2:
			v4 = v4+x
			x = x-5
			v4 = 7-v4
			paths.append(3)
		else:
			v4 = 2*v4
			v4 = v4*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))