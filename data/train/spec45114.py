import numpy as np 

def function(x):

	i6 = x
	x2 = 1
	paths = []
	try:
		if x2 > 1:
			x = 1/x
			i6 = i6*i6
			paths.append(1)
		else:
			x2 = 2*1
			paths.append(2)
		if x2 >= 0:
			x = 5-x
			x2 = x2*x
			i6 = 9/x
			paths.append(3)
		else:
			x2 = 1-i6
			x = 9*4
			x2 = 3+i6
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x = x2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))