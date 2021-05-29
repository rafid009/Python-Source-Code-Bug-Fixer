import numpy as np 

def function(x):

	f6 = 5
	x6 = x
	paths = []
	try:
		if x > 8:
			x6 = x6/x6
			x6 = x6/1
			paths.append(1)
		else:
			x = f6*x6
			x = x-x
			paths.append(2)
		if x >= 6:
			x6 = 9-3
			f6 = 7*5
			x = 4-f6
			paths.append(3)
		else:
			x6 = x6*6
			x = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))