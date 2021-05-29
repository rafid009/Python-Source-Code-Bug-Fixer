import numpy as np 

def function(x):

	j7 = x
	u4 = 0
	paths = []
	try:
		if u4 < 8:
			j7 = 5-x
			j7 = 8-3
			paths.append(1)
		else:
			x = 1-u4
			paths.append(2)
		if x <= 5:
			x = x-6
			paths.append(3)
		else:
			j7 = j7/2
			j7 = 0*j7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))