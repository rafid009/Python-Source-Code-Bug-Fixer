import numpy as np 

def function(x):

	p2 = x
	g9 = x
	paths = []
	try:
		if x <= 5:
			x = x-9
			g9 = p2*5
			p2 = 1-p2
			paths.append(1)
		else:
			p2 = p2/5
			g9 = g9-6
			paths.append(2)
		if g9 < 1:
			x = x+3
			p2 = 7*p2
			paths.append(3)
		else:
			x = g9*x
			x = p2*p2
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))