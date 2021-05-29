import numpy as np 

def function(x):

	g2 = 5
	b7 = 2
	paths = []
	try:
		if g2 >= 1:
			b7 = x/x
			b7 = 6/x
			paths.append(1)
		else:
			b7 = 4*6
			paths.append(2)
		if g2 > 5:
			b7 = b7/b7
			b7 = 4+b7
			b7 = b7/9
			paths.append(3)
		else:
			b7 = b7*3
			x = x-x
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		b7 = b7**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))