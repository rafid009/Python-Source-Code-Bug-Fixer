import numpy as np 

def function(x):

	g8 = 1
	k1 = 9
	paths = []
	try:
		if k1 < 7:
			x = x-3
			x = 6/x
			x = g8*g8
			paths.append(1)
		else:
			g8 = x/8
			k1 = x*8
			paths.append(2)
		if g8 < 7:
			g8 = g8*x
			g8 = g8-5
			g8 = x/g8
			paths.append(3)
		else:
			g8 = g8/1
			g8 = g8*g8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		k1 = g8**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))