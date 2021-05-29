import numpy as np 

def function(x):

	x3 = x
	v4 = 9
	paths = []
	try:
		if v4 < 9:
			x3 = x3*2
			x = x-9
			paths.append(1)
		else:
			v4 = 1+v4
			paths.append(2)
		if x < 1:
			v4 = 4/v4
			x = 2/1
			v4 = v4*9
			paths.append(3)
		else:
			x = x-7
			x3 = x3*v4
			x3 = 2-x3
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