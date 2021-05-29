import numpy as np 

def function(x):

	n5 = 1
	b5 = x
	paths = []
	try:
		if x <= 5:
			b5 = n5-x
			paths.append(1)
		else:
			n5 = 1+n5
			x = x/2
			x = 4/1
			paths.append(2)
		if x > 3:
			b5 = 6/8
			paths.append(3)
		else:
			b5 = 0-b5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))