import numpy as np 

def function(x):

	b5 = 2
	g4 = 2
	paths = []
	try:
		if x <= 2:
			g4 = g4*3
			paths.append(1)
		else:
			b5 = b5-5
			x = 9-x
			paths.append(2)
		if g4 > 8:
			b5 = 3-6
			x = x-7
			b5 = b5/3
			paths.append(3)
		else:
			b5 = g4*b5
			b5 = 5-b5
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))