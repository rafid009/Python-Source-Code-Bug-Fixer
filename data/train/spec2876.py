import numpy as np 

def function(x):

	x9 = x
	d6 = 9
	x = 1
	paths = []
	try:
		if x < 3:
			x9 = x9-8
			paths.append(1)
		else:
			x9 = x/7
			paths.append(2)
		if x > 0:
			x = x/6
			x9 = x9-0
			paths.append(3)
		else:
			x9 = x9/5
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))