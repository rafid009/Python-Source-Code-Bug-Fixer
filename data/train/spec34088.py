import numpy as np 

def function(x):

	b9 = x
	k5 = 7
	x = 4
	paths = []
	try:
		if x > 7:
			x = x*5
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if x > 6:
			x = 9*7
			paths.append(3)
		else:
			x = b9-3
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x = b9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))