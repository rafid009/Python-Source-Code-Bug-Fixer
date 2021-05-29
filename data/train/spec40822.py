import numpy as np 

def function(x):

	g2 = 5
	k0 = x
	x = x
	paths = []
	try:
		if x > 0:
			g2 = x/g2
			k0 = 4*8
			k0 = k0+g2
			paths.append(1)
		else:
			k0 = x+k0
			paths.append(2)
		if k0 > 9:
			g2 = g2-g2
			k0 = x+x
			paths.append(3)
		else:
			g2 = g2-x
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		x = k0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))