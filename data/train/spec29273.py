import numpy as np 

def function(x):

	x8 = 7
	n9 = x
	paths = []
	try:
		if n9 < 6:
			x8 = x-1
			x = 3/x
			x = x+2
			paths.append(1)
		else:
			n9 = n9*3
			x8 = x8-5
			paths.append(2)
		if x < 7:
			n9 = 9/n9
			x8 = 8-x8
			n9 = 6+x
			paths.append(3)
		else:
			n9 = n9-6
			x8 = x8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))