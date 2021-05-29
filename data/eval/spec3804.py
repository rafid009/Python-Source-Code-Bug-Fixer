import numpy as np 

def function(x):

	d1 = 1
	g2 = 7
	paths = []
	try:
		if g2 <= 2:
			d1 = d1/9
			g2 = 0/6
			x = x-6
			paths.append(1)
		else:
			d1 = x/5
			d1 = d1-7
			x = 5*x
			paths.append(2)
		if g2 >= 3:
			g2 = g2+7
			d1 = 6-5
			paths.append(3)
		else:
			g2 = g2/7
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