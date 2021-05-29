import numpy as np 

def function(x):

	q5 = 4
	g2 = x
	x = 5
	paths = []
	try:
		if g2 <= 0:
			g2 = q5-1
			paths.append(1)
		else:
			g2 = g2*8
			paths.append(2)
		if x <= 1:
			q5 = q5+5
			x = x/g2
			g2 = g2*x
			paths.append(3)
		else:
			x = g2+1
			q5 = q5*6
			x = 8-x
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