import numpy as np 

def function(x):

	v9 = 5
	l8 = 5
	paths = []
	try:
		if l8 <= 0:
			v9 = 1+5
			paths.append(1)
		else:
			l8 = 7-l8
			l8 = l8/9
			paths.append(2)
		if v9 >= 4:
			x = 8/x
			v9 = v9-v9
			paths.append(3)
		else:
			x = v9/l8
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