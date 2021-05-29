import numpy as np 

def function(x):

	n9 = x
	d1 = 9
	paths = []
	try:
		if d1 < 2:
			x = x-n9
			x = 1-x
			d1 = n9+4
			paths.append(1)
		else:
			n9 = n9-3
			x = 6-n9
			n9 = n9/5
			paths.append(2)
		if x >= 7:
			n9 = n9-9
			paths.append(3)
		else:
			x = x+7
			n9 = x/n9
			d1 = d1/d1
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