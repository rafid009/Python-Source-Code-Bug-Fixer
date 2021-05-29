import numpy as np 

def function(x):

	k1 = 4
	n1 = x
	paths = []
	try:
		if n1 > 7:
			n1 = 1+6
			k1 = k1/x
			k1 = k1*n1
			paths.append(1)
		else:
			k1 = 5+k1
			n1 = k1+n1
			k1 = k1*n1
			paths.append(2)
		if n1 > 9:
			n1 = 3+n1
			paths.append(3)
		else:
			k1 = 9*x
			k1 = x/k1
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