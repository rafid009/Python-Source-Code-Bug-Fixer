import numpy as np 

def function(x):

	t2 = x
	g2 = 9
	paths = []
	try:
		if g2 < 2:
			g2 = g2-9
			paths.append(1)
		else:
			x = 9+2
			x = x+5
			paths.append(2)
		if x <= 3:
			x = x+3
			t2 = 5*1
			x = 3/x
			paths.append(3)
		else:
			x = 8/t2
			g2 = 9*g2
			x = t2-x
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