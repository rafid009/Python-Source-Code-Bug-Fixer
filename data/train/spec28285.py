import numpy as np 

def function(x):

	v7 = x
	l8 = 5
	paths = []
	try:
		if x <= 6:
			l8 = 0-v7
			x = 4-x
			x = l8*x
			paths.append(1)
		else:
			v7 = x+7
			paths.append(2)
		if l8 >= 0:
			l8 = l8-x
			x = 7*x
			l8 = 6-v7
			paths.append(3)
		else:
			v7 = l8+5
			v7 = v7+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))