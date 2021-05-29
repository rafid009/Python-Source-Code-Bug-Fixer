import numpy as np 

def function(x):

	j5 = 5
	j1 = 6
	paths = []
	try:
		if x > 7:
			j5 = 9-j5
			x = 6+8
			x = j1/x
			paths.append(1)
		else:
			j5 = x-j5
			j5 = 2-5
			paths.append(2)
		if x > 6:
			x = 1/7
			j1 = j1-1
			paths.append(3)
		else:
			j1 = j1/j5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))