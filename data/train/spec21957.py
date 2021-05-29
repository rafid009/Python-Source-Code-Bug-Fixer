import numpy as np 

def function(x):

	r1 = x
	g2 = 7
	paths = []
	try:
		if g2 > 2:
			g2 = g2/8
			g2 = x-5
			g2 = g2-r1
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if r1 <= 0:
			r1 = r1+5
			paths.append(3)
		else:
			x = x+3
			r1 = 2/4
			g2 = g2/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))