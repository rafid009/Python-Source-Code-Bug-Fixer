import numpy as np 

def function(x):

	n9 = x
	n5 = x
	paths = []
	try:
		if n9 < 4:
			n5 = 8-n5
			n5 = 7+n5
			paths.append(1)
		else:
			n5 = 6/n5
			paths.append(2)
		if x < 7:
			x = n5/x
			x = x+n9
			x = x+n5
			paths.append(3)
		else:
			n5 = n5-9
			n9 = n9-4
			n5 = 5/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))