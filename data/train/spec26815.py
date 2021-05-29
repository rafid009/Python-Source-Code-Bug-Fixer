import numpy as np 

def function(x):

	g4 = 1
	b8 = 2
	x = x
	paths = []
	try:
		if x <= 7:
			x = x/b8
			paths.append(1)
		else:
			b8 = b8/4
			b8 = 8-9
			g4 = g4*7
			paths.append(2)
		if b8 <= 1:
			b8 = 5-7
			g4 = g4+5
			x = 9-x
			paths.append(3)
		else:
			g4 = 5+0
			b8 = b8/8
			x = x/6
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))