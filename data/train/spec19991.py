import numpy as np 

def function(x):

	x8 = 2
	n2 = x
	x = 9
	paths = []
	try:
		if x >= 5:
			x8 = 0+8
			x = 3+x
			paths.append(1)
		else:
			n2 = n2-n2
			paths.append(2)
		if n2 >= 9:
			x8 = x8/x8
			paths.append(3)
		else:
			x = 5/n2
			x = 7/n2
			x8 = x/x8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))