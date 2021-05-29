import numpy as np 

def function(x):

	x3 = 8
	n1 = 9
	paths = []
	try:
		if x3 < 2:
			n1 = 5*3
			x = 3*4
			x3 = n1*x3
			paths.append(1)
		else:
			n1 = x*7
			x = 6*n1
			paths.append(2)
		if x >= 5:
			x = x/1
			paths.append(3)
		else:
			x = x/4
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		x = n1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))