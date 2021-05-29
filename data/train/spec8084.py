import numpy as np 

def function(x):

	g7 = x
	k1 = 8
	x = 7
	paths = []
	try:
		if k1 > 7:
			k1 = 3+k1
			k1 = x*k1
			paths.append(1)
		else:
			x = x+g7
			x = 0+6
			k1 = k1/6
			paths.append(2)
		if g7 >= 0:
			k1 = k1/5
			paths.append(3)
		else:
			x = x-6
			g7 = g7/9
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		x = g7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))