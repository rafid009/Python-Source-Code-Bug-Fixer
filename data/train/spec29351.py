import numpy as np 

def function(x):

	g2 = x
	d2 = 8
	x = 5
	paths = []
	try:
		if g2 < 0:
			x = 8/4
			x = 8/x
			d2 = d2+g2
			paths.append(1)
		else:
			d2 = 9/6
			paths.append(2)
		if g2 > 6:
			d2 = d2*3
			g2 = g2+3
			paths.append(3)
		else:
			d2 = d2/6
			d2 = 5/d2
			x = d2*1
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