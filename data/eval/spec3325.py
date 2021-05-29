import numpy as np 

def function(x):

	v1 = x
	x3 = 1
	paths = []
	try:
		if x < 2:
			v1 = v1-1
			x = 9*v1
			paths.append(1)
		else:
			v1 = v1+2
			x3 = 8/x3
			paths.append(2)
		if x >= 8:
			v1 = v1*0
			x3 = 2*x3
			v1 = v1+v1
			paths.append(3)
		else:
			x3 = 5*x3
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