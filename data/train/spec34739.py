import numpy as np 

def function(x):

	n8 = 2
	l4 = 2
	paths = []
	try:
		if l4 <= 9:
			l4 = l4/9
			n8 = x+l4
			paths.append(1)
		else:
			n8 = 2+n8
			paths.append(2)
		if x < 5:
			n8 = 7/8
			paths.append(3)
		else:
			n8 = 1+7
			n8 = 5+n8
			l4 = l4*l4
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