import numpy as np 

def function(x):

	d9 = 2
	g1 = x
	paths = []
	try:
		if g1 > 8:
			x = g1+1
			paths.append(1)
		else:
			g1 = g1/1
			g1 = g1/2
			x = 9+9
			paths.append(2)
		if g1 < 5:
			d9 = d9*g1
			d9 = 4-d9
			g1 = 8*g1
			paths.append(3)
		else:
			d9 = d9+0
			x = d9-x
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