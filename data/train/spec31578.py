import numpy as np 

def function(x):

	l6 = 4
	n8 = 2
	x = 1
	paths = []
	try:
		if l6 > 8:
			n8 = n8/1
			l6 = l6+n8
			paths.append(1)
		else:
			x = n8/l6
			l6 = l6/l6
			n8 = x-n8
			paths.append(2)
		if l6 >= 4:
			n8 = 3-n8
			paths.append(3)
		else:
			n8 = 2*n8
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		x = n8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))