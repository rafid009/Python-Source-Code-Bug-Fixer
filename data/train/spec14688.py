import numpy as np 

def function(x):

	g5 = x
	b6 = x
	paths = []
	try:
		if x >= 0:
			x = g5-8
			paths.append(1)
		else:
			x = 9-6
			x = x+b6
			x = x+9
			paths.append(2)
		if x > 7:
			g5 = b6*g5
			g5 = g5*5
			paths.append(3)
		else:
			x = g5*x
			g5 = 9*g5
			g5 = b6/g5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))