import numpy as np 

def function(x):

	j6 = 4
	x6 = 8
	paths = []
	try:
		if x < 8:
			j6 = x6*j6
			j6 = j6/j6
			paths.append(1)
		else:
			x = x/j6
			x6 = 1/x6
			paths.append(2)
		if x < 5:
			x6 = j6*3
			x = x/x6
			x = 1/x
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))