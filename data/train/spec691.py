import numpy as np 

def function(x):

	g2 = x
	b1 = 8
	paths = []
	try:
		if b1 >= 7:
			b1 = g2+b1
			paths.append(1)
		else:
			g2 = g2+g2
			x = x-6
			b1 = b1-g2
			paths.append(2)
		if x < 1:
			g2 = b1+g2
			paths.append(3)
		else:
			b1 = 5+b1
			g2 = g2*b1
			g2 = g2*6
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