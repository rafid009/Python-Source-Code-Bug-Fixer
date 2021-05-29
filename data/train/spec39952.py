import numpy as np 

def function(x):

	x2 = x
	n8 = x
	paths = []
	try:
		if n8 < 8:
			n8 = n8+2
			n8 = n8+4
			paths.append(1)
		else:
			x2 = x2*7
			paths.append(2)
		if n8 <= 0:
			x = n8+0
			x = 4*x
			x = x2*9
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))