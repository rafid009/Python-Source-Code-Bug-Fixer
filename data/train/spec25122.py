import numpy as np 

def function(x):

	x1 = x
	x8 = 6
	paths = []
	try:
		if x8 < 4:
			x = x*x
			paths.append(1)
		else:
			x8 = x-x8
			x1 = x1*1
			paths.append(2)
		if x1 > 6:
			x1 = x1/1
			x = x1-8
			paths.append(3)
		else:
			x1 = x1+4
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x = x8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))