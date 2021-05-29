import numpy as np 

def function(x):

	k0 = 2
	g1 = x
	paths = []
	try:
		if g1 > 0:
			k0 = 5/8
			paths.append(1)
		else:
			k0 = 7/x
			paths.append(2)
		if x <= 9:
			x = 3+k0
			k0 = x+0
			paths.append(3)
		else:
			g1 = g1*k0
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