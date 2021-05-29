import numpy as np 

def function(x):

	k0 = x
	g1 = x
	x = 7
	paths = []
	try:
		if x < 2:
			x = x/k0
			x = x+0
			x = 9*g1
			paths.append(1)
		else:
			k0 = 7+g1
			paths.append(2)
		if g1 < 8:
			k0 = k0*6
			g1 = g1/5
			paths.append(3)
		else:
			x = x/6
			k0 = 0/k0
			x = x/7
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