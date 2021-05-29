import numpy as np 

def function(x):

	g1 = x
	k2 = 7
	paths = []
	try:
		if x < 8:
			k2 = k2-x
			g1 = 8*g1
			paths.append(1)
		else:
			x = x*8
			x = x/9
			paths.append(2)
		if x <= 6:
			x = 4*5
			k2 = x*k2
			k2 = 2*x
			paths.append(3)
		else:
			g1 = 0*7
			x = 8-x
			g1 = g1/7
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