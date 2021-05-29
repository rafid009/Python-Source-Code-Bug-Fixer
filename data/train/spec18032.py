import numpy as np 

def function(x):

	b4 = 5
	x6 = 0
	x = x
	paths = []
	try:
		if x < 5:
			x6 = 9-x6
			paths.append(1)
		else:
			b4 = 6-b4
			paths.append(2)
		if x6 <= 9:
			b4 = b4/6
			paths.append(3)
		else:
			x6 = 4*x6
			b4 = b4*b4
			x = 7-x
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