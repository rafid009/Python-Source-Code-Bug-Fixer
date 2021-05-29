import numpy as np 

def function(x):

	n3 = 1
	g1 = x
	paths = []
	try:
		if x < 8:
			n3 = 3+n3
			paths.append(1)
		else:
			x = 0-g1
			paths.append(2)
		if n3 <= 7:
			g1 = 3/g1
			n3 = n3+x
			n3 = n3+1
			paths.append(3)
		else:
			x = 8*n3
			n3 = g1*4
			x = x/8
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