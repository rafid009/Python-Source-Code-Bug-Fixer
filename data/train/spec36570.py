import numpy as np 

def function(x):

	g2 = 3
	l9 = x
	paths = []
	try:
		if x < 1:
			l9 = l9+g2
			paths.append(1)
		else:
			l9 = l9/3
			g2 = g2*2
			paths.append(2)
		if g2 <= 2:
			g2 = g2*8
			l9 = l9-8
			x = 2/g2
			paths.append(3)
		else:
			g2 = g2+5
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		g2 = l9**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))