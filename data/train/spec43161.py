import numpy as np 

def function(x):

	p4 = x
	g3 = x
	paths = []
	try:
		if g3 >= 0:
			x = 9/g3
			paths.append(1)
		else:
			x = g3+1
			g3 = p4/1
			g3 = x*g3
			paths.append(2)
		if x <= 6:
			x = 3/x
			x = p4/x
			x = p4-x
			paths.append(3)
		else:
			x = x-5
			p4 = 8*g3
			p4 = 1+g3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g3 = x**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))