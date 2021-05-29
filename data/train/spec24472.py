import numpy as np 

def function(x):

	n7 = 2
	n6 = x
	x = 3
	paths = []
	try:
		if x >= 4:
			n7 = n6-n7
			n6 = n6+x
			paths.append(1)
		else:
			n7 = n7-6
			paths.append(2)
		if x <= 9:
			n7 = n7+5
			paths.append(3)
		else:
			n7 = n6-x
			n6 = n6*n6
			n7 = x+n7
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		n7 = n6**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))