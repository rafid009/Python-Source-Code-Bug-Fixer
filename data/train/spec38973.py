import numpy as np 

def function(x):

	n9 = x
	q8 = 9
	paths = []
	try:
		if n9 >= 6:
			q8 = 1/q8
			paths.append(1)
		else:
			n9 = n9+x
			x = 4/x
			n9 = 8/2
			paths.append(2)
		if q8 <= 9:
			x = x+3
			n9 = n9-8
			paths.append(3)
		else:
			x = x-n9
			n9 = 3+n9
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