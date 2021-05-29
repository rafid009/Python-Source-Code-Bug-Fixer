import numpy as np 

def function(x):

	x2 = x
	n5 = 9
	paths = []
	try:
		if n5 >= 2:
			n5 = n5/5
			paths.append(1)
		else:
			x2 = x-8
			n5 = 9*x
			paths.append(2)
		if x >= 7:
			n5 = 6/n5
			x2 = 4*6
			x2 = n5/n5
			paths.append(3)
		else:
			x = x2+x
			n5 = n5-4
			n5 = x+4
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