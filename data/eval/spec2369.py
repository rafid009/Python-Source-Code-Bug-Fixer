import numpy as np 

def function(x):

	n2 = x
	u1 = 9
	paths = []
	try:
		if x < 0:
			n2 = 9*n2
			paths.append(1)
		else:
			u1 = u1/3
			n2 = 0*7
			n2 = 9+7
			paths.append(2)
		if n2 >= 3:
			n2 = n2*n2
			n2 = 0+7
			paths.append(3)
		else:
			u1 = 6/n2
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		n2 = u1**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))