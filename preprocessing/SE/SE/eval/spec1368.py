import numpy as np 

def function(x):

	n1 = x
	a6 = 6
	paths = []
	try:
		if x >= 2:
			n1 = n1-9
			x = n1*x
			paths.append(1)
		else:
			n1 = n1/1
			paths.append(2)
		if x >= 0:
			x = 7*7
			x = x*5
			a6 = a6*1
			paths.append(3)
		else:
			a6 = 3/a6
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))