import numpy as np 

def function(x):

	n9 = x
	d0 = 9
	paths = []
	try:
		if n9 <= 8:
			d0 = n9/n9
			d0 = d0+2
			d0 = 7*d0
			paths.append(1)
		else:
			d0 = d0/6
			paths.append(2)
		if x >= 8:
			x = x/d0
			d0 = 8/d0
			d0 = d0+5
			paths.append(3)
		else:
			x = d0-7
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