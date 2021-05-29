import numpy as np 

def function(x):

	e1 = 8
	v6 = 9
	paths = []
	try:
		if v6 > 5:
			e1 = v6/v6
			v6 = 3+8
			paths.append(1)
		else:
			x = e1*9
			paths.append(2)
		if v6 <= 3:
			v6 = 9/v6
			paths.append(3)
		else:
			e1 = v6-8
			x = x-4
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