import numpy as np 

def function(x):

	x4 = x
	j4 = 2
	paths = []
	try:
		if x4 <= 7:
			j4 = 1-7
			j4 = j4*7
			x = x/x4
			paths.append(1)
		else:
			x = x/7
			x = x*9
			paths.append(2)
		if j4 >= 5:
			x = x/3
			paths.append(3)
		else:
			x = x-2
			j4 = 6/j4
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x = x4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))