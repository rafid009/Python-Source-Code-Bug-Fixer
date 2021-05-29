import numpy as np 

def function(x):

	g5 = 8
	b7 = x
	paths = []
	try:
		if x < 4:
			x = x+x
			b7 = b7+7
			b7 = b7-x
			paths.append(1)
		else:
			b7 = b7-x
			b7 = 9-4
			x = x/7
			paths.append(2)
		if x >= 2:
			g5 = 6-6
			paths.append(3)
		else:
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))