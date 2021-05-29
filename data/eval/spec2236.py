import numpy as np 

def function(x):

	n0 = x
	g5 = 2
	paths = []
	try:
		if n0 <= 6:
			g5 = x*3
			paths.append(1)
		else:
			n0 = n0-4
			paths.append(2)
		if x < 5:
			x = n0/g5
			x = x+6
			n0 = g5/n0
			paths.append(3)
		else:
			x = x/g5
			n0 = 2+n0
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