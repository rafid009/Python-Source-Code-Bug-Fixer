import numpy as np 

def function(x):

	y5 = 8
	v1 = 1
	paths = []
	try:
		if y5 <= 1:
			y5 = y5/2
			paths.append(1)
		else:
			v1 = x/v1
			paths.append(2)
		if y5 > 4:
			y5 = y5+8
			v1 = v1*y5
			v1 = 5+6
			paths.append(3)
		else:
			x = v1/8
			y5 = v1+6
			x = v1/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v1 = x**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))