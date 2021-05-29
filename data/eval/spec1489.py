import numpy as np 

def function(x):

	b7 = x
	g2 = x
	x = x
	paths = []
	try:
		if g2 >= 2:
			b7 = 4+b7
			g2 = g2-3
			b7 = g2+b7
			paths.append(1)
		else:
			b7 = 6+x
			b7 = b7/1
			g2 = g2-g2
			paths.append(2)
		if x >= 8:
			b7 = b7/1
			paths.append(3)
		else:
			x = g2+g2
			x = x*6
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