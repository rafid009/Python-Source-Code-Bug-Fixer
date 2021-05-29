import numpy as np 

def function(x):

	v3 = x
	v6 = 7
	paths = []
	try:
		if v3 >= 2:
			v3 = 9*4
			paths.append(1)
		else:
			v6 = 1*6
			paths.append(2)
		if v6 <= 6:
			v3 = v3-x
			v6 = 3+v6
			v6 = 7+4
			paths.append(3)
		else:
			v3 = 4+3
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