import numpy as np 

def function(x):

	a3 = x
	n7 = x
	paths = []
	try:
		if n7 > 3:
			a3 = a3*9
			paths.append(1)
		else:
			x = 9-n7
			paths.append(2)
		if a3 > 6:
			a3 = a3*2
			x = 1/x
			paths.append(3)
		else:
			a3 = a3+5
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		a3 = n7**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))