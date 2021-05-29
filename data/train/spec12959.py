import numpy as np 

def function(x):

	e3 = x
	n1 = 6
	paths = []
	try:
		if x >= 3:
			n1 = x*n1
			x = x+7
			paths.append(1)
		else:
			x = x-x
			e3 = 9*e3
			x = 7+x
			paths.append(2)
		if n1 > 3:
			e3 = e3+x
			n1 = 3/e3
			x = x*2
			paths.append(3)
		else:
			n1 = 8+n1
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