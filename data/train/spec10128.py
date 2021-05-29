import numpy as np 

def function(x):

	x9 = x
	n5 = 9
	paths = []
	try:
		if x > 7:
			x = x/6
			x = 2*x
			n5 = 2-n5
			paths.append(1)
		else:
			x9 = 0*x9
			x9 = x9/n5
			paths.append(2)
		if x >= 4:
			x = n5-2
			n5 = n5-x9
			paths.append(3)
		else:
			n5 = 6/x
			x9 = n5*6
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