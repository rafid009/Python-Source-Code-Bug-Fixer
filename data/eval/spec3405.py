import numpy as np 

def function(x):

	n1 = 8
	a4 = 4
	paths = []
	try:
		if n1 <= 0:
			n1 = n1/x
			a4 = a4-a4
			paths.append(1)
		else:
			a4 = a4/7
			paths.append(2)
		if n1 < 9:
			a4 = x-6
			paths.append(3)
		else:
			a4 = 1-2
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))