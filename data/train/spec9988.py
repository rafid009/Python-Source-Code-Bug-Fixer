import numpy as np 

def function(x):

	g1 = x
	p4 = 7
	paths = []
	try:
		if p4 > 9:
			g1 = g1/7
			paths.append(1)
		else:
			x = p4/x
			paths.append(2)
		if g1 <= 2:
			x = 3/g1
			x = x-1
			paths.append(3)
		else:
			g1 = g1-g1
			p4 = 8+4
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))