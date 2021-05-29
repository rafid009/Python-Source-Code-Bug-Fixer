import numpy as np 

def function(x):

	g2 = x
	b0 = x
	paths = []
	try:
		if x > 3:
			x = 4+3
			paths.append(1)
		else:
			b0 = g2*9
			paths.append(2)
		if b0 <= 8:
			g2 = x/g2
			x = 4/b0
			paths.append(3)
		else:
			x = x/8
			x = 4/x
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