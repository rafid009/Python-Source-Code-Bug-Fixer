import numpy as np 

def function(x):

	v9 = 9
	x2 = x
	paths = []
	try:
		if v9 <= 7:
			v9 = v9*9
			x2 = 8+x2
			paths.append(1)
		else:
			x = x2/v9
			x2 = v9-x2
			v9 = v9+8
			paths.append(2)
		if v9 >= 8:
			x = 5/x2
			paths.append(3)
		else:
			x2 = x2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))