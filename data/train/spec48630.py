import numpy as np 

def function(x):

	x3 = 5
	x9 = 7
	paths = []
	try:
		if x <= 2:
			x3 = x3+9
			paths.append(1)
		else:
			x = x/x3
			x = 1-x
			x3 = x9+x
			paths.append(2)
		if x9 > 2:
			x3 = x3+5
			x9 = 6*9
			x = 7+0
			paths.append(3)
		else:
			x = x+x3
			x9 = 0/8
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))