import numpy as np 

def function(x):

	n1 = 5
	k4 = 5
	paths = []
	try:
		if k4 > 8:
			k4 = n1*k4
			n1 = 3/7
			paths.append(1)
		else:
			n1 = 3/n1
			k4 = 5*6
			paths.append(2)
		if k4 < 6:
			x = k4*7
			x = 6+4
			paths.append(3)
		else:
			n1 = 2-n1
			n1 = n1-x
			x = n1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))