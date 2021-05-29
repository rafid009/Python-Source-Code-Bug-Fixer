import numpy as np 

def function(x):

	k0 = 8
	g4 = x
	paths = []
	try:
		if x <= 1:
			k0 = 4*k0
			x = x*1
			k0 = x*6
			paths.append(1)
		else:
			k0 = k0*k0
			x = 2+x
			paths.append(2)
		if x <= 0:
			g4 = x*g4
			x = x*2
			g4 = x-6
			paths.append(3)
		else:
			x = x+6
			g4 = 9/g4
			x = k0/x
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		g4 = k0**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))