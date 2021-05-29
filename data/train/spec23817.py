import numpy as np 

def function(x):

	e9 = x
	x9 = 4
	paths = []
	try:
		if x >= 8:
			x = x-1
			e9 = e9*x9
			paths.append(1)
		else:
			e9 = 6/e9
			x = 9/6
			paths.append(2)
		if x > 1:
			x9 = x9+0
			paths.append(3)
		else:
			e9 = e9+9
			x = x-5
			x = 8/5
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x9 = e9**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))