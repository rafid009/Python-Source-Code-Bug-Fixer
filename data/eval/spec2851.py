import numpy as np 

def function(x):

	g6 = x
	b3 = x
	paths = []
	try:
		if g6 >= 6:
			b3 = b3/6
			g6 = 1+g6
			paths.append(1)
		else:
			b3 = x+x
			paths.append(2)
		if b3 >= 9:
			g6 = g6*5
			x = x-x
			paths.append(3)
		else:
			x = b3*g6
			b3 = b3/9
			x = x*b3
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		b3 = b3**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))