import numpy as np 

def function(x):

	g7 = x
	b7 = 6
	paths = []
	try:
		if b7 >= 8:
			b7 = b7+3
			x = x*1
			paths.append(1)
		else:
			b7 = 7/b7
			b7 = b7-5
			paths.append(2)
		if g7 > 5:
			b7 = b7-x
			paths.append(3)
		else:
			x = x/5
			g7 = 2+x
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		g7 = b7**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))