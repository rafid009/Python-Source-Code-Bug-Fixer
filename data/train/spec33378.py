import numpy as np 

def function(x):

	b8 = 0
	n9 = 1
	paths = []
	try:
		if n9 <= 0:
			n9 = 2-n9
			x = n9+8
			b8 = b8+6
			paths.append(1)
		else:
			b8 = b8*x
			paths.append(2)
		if n9 >= 5:
			n9 = 0/2
			n9 = n9/n9
			b8 = x-n9
			paths.append(3)
		else:
			n9 = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))