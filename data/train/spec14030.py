import numpy as np 

def function(x):

	n9 = 8
	x3 = 6
	paths = []
	try:
		if x3 < 1:
			n9 = 3*n9
			paths.append(1)
		else:
			x3 = x3-8
			x3 = x3-x
			x = 8*x
			paths.append(2)
		if x <= 5:
			n9 = 7+3
			x = x-1
			paths.append(3)
		else:
			n9 = n9*8
			x = 3+2
			x = x+0
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		n9 = x3**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))