import numpy as np 

def function(x):

	a7 = 2
	n1 = 2
	paths = []
	try:
		if x < 6:
			n1 = n1*a7
			n1 = 9-n1
			x = 4+a7
			paths.append(1)
		else:
			a7 = a7-9
			n1 = n1/5
			n1 = 2*a7
			paths.append(2)
		if x >= 3:
			a7 = n1+4
			paths.append(3)
		else:
			n1 = 6/n1
			x = 8/x
			a7 = a7*n1
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		a7 = n1**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))