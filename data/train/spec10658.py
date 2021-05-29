import numpy as np 

def function(x):

	x3 = 1
	b7 = x
	paths = []
	try:
		if x > 9:
			x = 9-2
			x = b7+x
			b7 = 1/b7
			paths.append(1)
		else:
			b7 = b7+x
			x = x+7
			paths.append(2)
		if x > 8:
			x = 0-b7
			x3 = x3-x
			paths.append(3)
		else:
			x3 = 6/x3
			x3 = x3+x
			x = x+0
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x = x3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))