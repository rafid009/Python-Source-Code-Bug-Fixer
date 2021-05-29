import numpy as np 

def function(x):

	g7 = 5
	n2 = 4
	paths = []
	try:
		if x < 6:
			n2 = 6-n2
			n2 = n2-2
			n2 = n2-5
			paths.append(1)
		else:
			n2 = 0+n2
			x = 5/n2
			paths.append(2)
		if g7 <= 7:
			n2 = n2/g7
			g7 = x*8
			paths.append(3)
		else:
			n2 = n2*7
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		g7 = g7**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))