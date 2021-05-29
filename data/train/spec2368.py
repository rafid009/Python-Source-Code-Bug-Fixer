import numpy as np 

def function(x):

	u6 = x
	n1 = 1
	paths = []
	try:
		if u6 < 2:
			n1 = n1*2
			u6 = 7/x
			paths.append(1)
		else:
			x = x-n1
			paths.append(2)
		if x >= 5:
			n1 = 4*n1
			x = n1/x
			x = x/9
			paths.append(3)
		else:
			n1 = 9*n1
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