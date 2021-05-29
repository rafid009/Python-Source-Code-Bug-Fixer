import numpy as np 

def function(x):

	j4 = x
	u4 = x
	paths = []
	try:
		if x > 1:
			x = x-u4
			paths.append(1)
		else:
			u4 = 1+j4
			paths.append(2)
		if j4 <= 9:
			j4 = 8+3
			paths.append(3)
		else:
			x = 2*x
			u4 = 6-j4
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