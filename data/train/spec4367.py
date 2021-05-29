import numpy as np 

def function(x):

	n4 = 5
	o1 = 6
	paths = []
	try:
		if x > 5:
			x = 4*x
			paths.append(1)
		else:
			n4 = 6/o1
			o1 = x+o1
			paths.append(2)
		if o1 <= 3:
			n4 = 0+0
			paths.append(3)
		else:
			n4 = n4-4
			x = 8-4
			x = 9+n4
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		n4 = n4**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))