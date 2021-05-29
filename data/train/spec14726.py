import numpy as np 

def function(x):

	d8 = x
	n9 = 9
	paths = []
	try:
		if x >= 2:
			x = x/3
			paths.append(1)
		else:
			d8 = d8-5
			paths.append(2)
		if n9 < 0:
			d8 = 5+4
			x = 0+x
			n9 = 1/n9
			paths.append(3)
		else:
			n9 = n9*d8
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		x = n9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))