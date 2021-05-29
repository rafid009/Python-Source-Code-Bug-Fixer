import numpy as np 

def function(x):

	n5 = x
	n3 = x
	paths = []
	try:
		if n3 < 1:
			x = 6+n5
			n3 = n3+2
			paths.append(1)
		else:
			n3 = 9-4
			paths.append(2)
		if n3 <= 9:
			n3 = 0-x
			paths.append(3)
		else:
			n3 = n3-4
			n5 = n3+3
			n3 = n3-0
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))