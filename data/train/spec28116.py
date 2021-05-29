import numpy as np 

def function(x):

	j9 = x
	j7 = x
	paths = []
	try:
		if x >= 1:
			j7 = x*j7
			paths.append(1)
		else:
			j9 = 2/j9
			paths.append(2)
		if j9 < 1:
			x = 4-x
			paths.append(3)
		else:
			j7 = x/j7
			x = j7+j9
			x = j9-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))