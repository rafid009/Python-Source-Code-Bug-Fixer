import numpy as np 

def function(x):

	k5 = 1
	g5 = x
	paths = []
	try:
		if g5 >= 0:
			x = 4*x
			paths.append(1)
		else:
			x = 2+2
			g5 = g5+x
			x = 9/x
			paths.append(2)
		if k5 <= 1:
			k5 = 2*k5
			x = 0/x
			paths.append(3)
		else:
			g5 = g5-3
			g5 = k5/8
			k5 = 4*k5
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		x = g5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))