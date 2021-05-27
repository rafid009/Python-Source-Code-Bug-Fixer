import numpy as np 

def function(x):

	n7 = x
	g0 = x
	paths = []
	try:
		if x >= 8:
			n7 = n7+6
			g0 = 6/g0
			paths.append(1)
		else:
			n7 = n7*x
			paths.append(2)
		if n7 > 5:
			x = x-8
			paths.append(3)
		else:
			n7 = 1/n7
			x = 7+x
			x = x-5
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