import numpy as np 

def function(x):

	x9 = 6
	i1 = x
	paths = []
	try:
		if x9 < 3:
			x = 1*x
			paths.append(1)
		else:
			x9 = x9-9
			paths.append(2)
		if x < 8:
			x = x*6
			x9 = x9/7
			x9 = x9/x
			paths.append(3)
		else:
			i1 = x-5
			x9 = 9/i1
			x = x-9
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x9 = i1**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))