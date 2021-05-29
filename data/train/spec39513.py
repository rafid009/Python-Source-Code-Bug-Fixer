import numpy as np 

def function(x):

	v5 = 8
	x3 = x
	x = x
	paths = []
	try:
		if x3 < 0:
			x3 = x3/x3
			v5 = x3/5
			paths.append(1)
		else:
			x = x+6
			x = 4/x
			paths.append(2)
		if v5 >= 4:
			v5 = v5*3
			paths.append(3)
		else:
			v5 = 4+3
			v5 = 9/v5
			v5 = v5/5
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