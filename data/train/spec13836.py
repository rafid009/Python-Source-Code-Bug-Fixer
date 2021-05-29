import numpy as np 

def function(x):

	n9 = x
	n4 = 3
	paths = []
	try:
		if n9 <= 0:
			n4 = n4-7
			x = x+7
			paths.append(1)
		else:
			n9 = n9+2
			n4 = 8-x
			paths.append(2)
		if x > 3:
			x = 2*8
			x = n9*x
			paths.append(3)
		else:
			n4 = x-4
			n4 = 1-0
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		n9 = n9**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))