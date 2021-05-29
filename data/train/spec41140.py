import numpy as np 

def function(x):

	x5 = x
	v5 = 0
	paths = []
	try:
		if v5 >= 6:
			v5 = x+6
			v5 = v5+4
			paths.append(1)
		else:
			x = 5-8
			paths.append(2)
		if x5 <= 1:
			v5 = 3-x5
			x5 = 6+8
			x5 = 7+v5
			paths.append(3)
		else:
			v5 = 1*6
			x = x5*9
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