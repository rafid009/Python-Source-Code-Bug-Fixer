import numpy as np 

def function(x):

	y5 = x
	n2 = 3
	paths = []
	try:
		if y5 <= 0:
			x = x+2
			y5 = y5-3
			x = y5*x
			paths.append(1)
		else:
			x = 8*x
			y5 = y5/7
			n2 = x/4
			paths.append(2)
		if x <= 5:
			n2 = x+y5
			y5 = 8-y5
			y5 = y5+8
			paths.append(3)
		else:
			y5 = y5-3
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