import numpy as np 

def function(x):

	x2 = x
	d9 = x
	paths = []
	try:
		if x < 5:
			x2 = 6/x2
			paths.append(1)
		else:
			x = 1*1
			paths.append(2)
		if x2 < 0:
			d9 = 3+7
			d9 = 2/d9
			paths.append(3)
		else:
			d9 = d9-d9
			x = 4*x
			x2 = x2+7
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