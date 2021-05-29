import numpy as np 

def function(x):

	t7 = 8
	n7 = x
	paths = []
	try:
		if t7 > 9:
			x = x*5
			paths.append(1)
		else:
			n7 = n7/9
			paths.append(2)
		if t7 < 1:
			n7 = 7*n7
			paths.append(3)
		else:
			x = 7*x
			n7 = n7/2
			n7 = 5-t7
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