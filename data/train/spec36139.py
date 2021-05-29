import numpy as np 

def function(x):

	l0 = x
	n8 = 8
	paths = []
	try:
		if l0 <= 5:
			l0 = x+3
			n8 = n8+6
			paths.append(1)
		else:
			l0 = 1/6
			n8 = n8+l0
			paths.append(2)
		if x < 5:
			x = 4+0
			x = l0*x
			l0 = 3/2
			paths.append(3)
		else:
			n8 = 6*x
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