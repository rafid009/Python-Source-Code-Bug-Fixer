import numpy as np 

def function(x):

	j4 = x
	x9 = 2
	paths = []
	try:
		if x >= 8:
			x9 = x9-x
			paths.append(1)
		else:
			x = x*3
			x = x-8
			paths.append(2)
		if x9 >= 0:
			x = 2-1
			paths.append(3)
		else:
			x9 = x9-0
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		j4 = x9**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))