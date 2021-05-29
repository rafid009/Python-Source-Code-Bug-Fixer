import numpy as np 

def function(x):

	n8 = x
	i8 = x
	paths = []
	try:
		if x >= 9:
			i8 = x/4
			n8 = x/3
			paths.append(1)
		else:
			i8 = n8/i8
			paths.append(2)
		if n8 < 0:
			x = 7+5
			x = 1*x
			paths.append(3)
		else:
			i8 = 2-x
			x = 9+i8
			x = n8-1
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		n8 = n8**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))