import numpy as np 

def function(x):

	n1 = 9
	u3 = x
	paths = []
	try:
		if n1 >= 2:
			u3 = u3-8
			n1 = 6-x
			paths.append(1)
		else:
			n1 = n1/u3
			paths.append(2)
		if n1 <= 1:
			u3 = 8/u3
			paths.append(3)
		else:
			x = 9*x
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