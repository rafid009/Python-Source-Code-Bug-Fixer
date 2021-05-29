import numpy as np 

def function(x):

	n3 = x
	d7 = 0
	paths = []
	try:
		if x < 6:
			n3 = 9*n3
			paths.append(1)
		else:
			d7 = d7+x
			d7 = x+x
			x = 6/x
			paths.append(2)
		if d7 >= 9:
			d7 = x*3
			d7 = d7-7
			x = 3+x
			paths.append(3)
		else:
			n3 = n3*n3
			d7 = 2-d7
			n3 = n3+d7
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		x = d7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))