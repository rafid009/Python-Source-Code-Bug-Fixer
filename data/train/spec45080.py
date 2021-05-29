import numpy as np 

def function(x):

	p4 = 6
	g1 = x
	paths = []
	try:
		if g1 >= 8:
			g1 = g1*8
			paths.append(1)
		else:
			p4 = 3/p4
			p4 = 9-0
			paths.append(2)
		if x <= 0:
			x = p4+x
			paths.append(3)
		else:
			g1 = 2+g1
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		g1 = g1**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))