import numpy as np 

def function(x):

	r5 = 8
	g2 = 4
	paths = []
	try:
		if g2 <= 3:
			g2 = g2/1
			paths.append(1)
		else:
			r5 = r5+r5
			paths.append(2)
		if x > 6:
			g2 = g2/3
			paths.append(3)
		else:
			x = g2/x
			x = x/1
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