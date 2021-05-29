import numpy as np 

def function(x):

	n7 = 5
	g2 = x
	paths = []
	try:
		if n7 > 9:
			x = x*1
			x = x-5
			n7 = n7/5
			paths.append(1)
		else:
			x = x/9
			g2 = g2*g2
			paths.append(2)
		if n7 <= 2:
			n7 = 8+g2
			paths.append(3)
		else:
			n7 = 9/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g2 = x**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))