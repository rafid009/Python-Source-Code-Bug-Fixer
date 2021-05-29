import numpy as np 

def function(x):

	x5 = 3
	x9 = 9
	paths = []
	try:
		if x > 0:
			x5 = x5-7
			paths.append(1)
		else:
			x = 4/x
			x5 = x5+0
			x9 = 3-x9
			paths.append(2)
		if x9 >= 5:
			x9 = x9/9
			x9 = x/x9
			paths.append(3)
		else:
			x = 7+7
			x9 = 3-7
			x = x-x
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x5 = x9**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))