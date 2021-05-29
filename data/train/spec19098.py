import numpy as np 

def function(x):

	n2 = 9
	y3 = 1
	paths = []
	try:
		if x < 5:
			x = 7*x
			paths.append(1)
		else:
			n2 = n2-7
			paths.append(2)
		if x < 2:
			n2 = n2-x
			paths.append(3)
		else:
			x = x-n2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))