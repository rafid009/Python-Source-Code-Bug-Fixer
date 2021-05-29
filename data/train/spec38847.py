import numpy as np 

def function(x):

	g6 = x
	k1 = 6
	paths = []
	try:
		if g6 >= 8:
			x = x-9
			paths.append(1)
		else:
			k1 = k1+4
			k1 = 0+g6
			x = 5*x
			paths.append(2)
		if g6 > 4:
			g6 = 6*6
			x = 0*x
			paths.append(3)
		else:
			x = 2+0
			x = x*2
			x = x*4
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		k1 = g6**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))