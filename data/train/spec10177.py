import numpy as np 

def function(x):

	x3 = 0
	e6 = 3
	paths = []
	try:
		if e6 >= 0:
			e6 = 0-e6
			paths.append(1)
		else:
			x = 7*x
			paths.append(2)
		if e6 <= 8:
			x3 = x+x3
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x3 = e6**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))