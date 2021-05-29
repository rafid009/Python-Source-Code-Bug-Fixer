import numpy as np 

def function(x):

	n7 = 4
	q8 = 4
	paths = []
	try:
		if q8 >= 1:
			q8 = 7+3
			paths.append(1)
		else:
			n7 = 4/n7
			n7 = x/6
			paths.append(2)
		if x > 0:
			x = 9-x
			paths.append(3)
		else:
			x = x*2
			q8 = 7/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))