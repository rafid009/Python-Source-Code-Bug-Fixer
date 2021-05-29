import numpy as np 

def function(x):

	g1 = x
	b7 = 4
	paths = []
	try:
		if g1 > 4:
			x = b7-x
			paths.append(1)
		else:
			b7 = 4+9
			b7 = b7+1
			paths.append(2)
		if x > 6:
			x = x/6
			g1 = g1-g1
			paths.append(3)
		else:
			b7 = 4/b7
			x = x+1
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