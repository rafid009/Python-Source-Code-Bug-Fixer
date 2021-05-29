import numpy as np 

def function(x):

	a7 = 4
	n4 = x
	x = x
	paths = []
	try:
		if a7 < 9:
			n4 = n4*4
			n4 = 7-n4
			n4 = 0*7
			paths.append(1)
		else:
			a7 = 8+3
			n4 = n4+n4
			a7 = 6*a7
			paths.append(2)
		if x < 9:
			a7 = n4-7
			n4 = a7+6
			paths.append(3)
		else:
			a7 = a7*5
			a7 = a7/5
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))