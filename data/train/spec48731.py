import numpy as np 

def function(x):

	n8 = 7
	m5 = 6
	paths = []
	try:
		if n8 > 6:
			x = 8+7
			x = 0-x
			paths.append(1)
		else:
			n8 = n8/9
			paths.append(2)
		if n8 > 8:
			x = 1-x
			x = 0/x
			paths.append(3)
		else:
			n8 = 8*x
			m5 = 3/8
			n8 = 8+9
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