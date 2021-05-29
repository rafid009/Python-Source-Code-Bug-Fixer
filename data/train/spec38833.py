import numpy as np 

def function(x):

	n1 = x
	n7 = 3
	paths = []
	try:
		if x <= 8:
			n1 = 6*n1
			n1 = n1/n1
			paths.append(1)
		else:
			n1 = 2*2
			x = x*n7
			n7 = n7+n7
			paths.append(2)
		if n7 <= 5:
			n1 = 8*n1
			paths.append(3)
		else:
			n1 = 6+n1
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