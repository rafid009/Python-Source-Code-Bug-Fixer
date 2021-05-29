import numpy as np 

def function(x):

	n5 = x
	l4 = x
	paths = []
	try:
		if x <= 7:
			l4 = l4+l4
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if x <= 3:
			l4 = l4+0
			paths.append(3)
		else:
			x = x-8
			l4 = 6+6
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		x = n5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))