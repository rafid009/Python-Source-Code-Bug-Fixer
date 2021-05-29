import numpy as np 

def function(x):

	n5 = x
	x1 = x
	paths = []
	try:
		if x1 >= 7:
			x1 = x*6
			x = x-4
			n5 = n5-8
			paths.append(1)
		else:
			n5 = n5-6
			x = x/1
			paths.append(2)
		if x1 >= 3:
			x = x+x1
			paths.append(3)
		else:
			n5 = x-2
			x = 0-x
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		n5 = x1**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))