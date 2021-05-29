import numpy as np 

def function(x):

	d1 = x
	g2 = x
	paths = []
	try:
		if g2 < 7:
			g2 = x+3
			paths.append(1)
		else:
			d1 = x/d1
			paths.append(2)
		if g2 <= 3:
			d1 = 5/x
			paths.append(3)
		else:
			g2 = 3-g2
			d1 = 8+d1
			x = x/x
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