import numpy as np 

def function(x):

	a3 = x
	x8 = x
	paths = []
	try:
		if x >= 0:
			a3 = 1/x8
			a3 = a3*7
			paths.append(1)
		else:
			a3 = x8+a3
			x8 = 7+x8
			a3 = 5+x
			paths.append(2)
		if x <= 2:
			x = x+4
			paths.append(3)
		else:
			x = 2+7
			a3 = a3-9
			x8 = 6*a3
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x8 = x8**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))