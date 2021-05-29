import numpy as np 

def function(x):

	e6 = 6
	n1 = 6
	paths = []
	try:
		if x < 3:
			x = n1+x
			e6 = 3/1
			paths.append(1)
		else:
			n1 = n1*n1
			x = n1+e6
			paths.append(2)
		if x <= 3:
			x = x+6
			x = e6+x
			e6 = 1+e6
			paths.append(3)
		else:
			n1 = n1-x
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