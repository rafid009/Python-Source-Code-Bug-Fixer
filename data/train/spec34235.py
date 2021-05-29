import numpy as np 

def function(x):

	n8 = x
	l8 = x
	paths = []
	try:
		if x > 6:
			n8 = n8*9
			l8 = l8*l8
			x = n8+l8
			paths.append(1)
		else:
			x = x+5
			x = 3+x
			paths.append(2)
		if l8 >= 2:
			l8 = l8-2
			l8 = x-0
			n8 = n8*3
			paths.append(3)
		else:
			l8 = 3/x
			n8 = x/n8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))