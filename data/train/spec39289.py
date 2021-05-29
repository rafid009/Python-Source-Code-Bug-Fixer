import numpy as np 

def function(x):

	k7 = x
	d9 = x
	paths = []
	try:
		if d9 > 4:
			x = x/d9
			x = 8/x
			paths.append(1)
		else:
			d9 = 9+x
			d9 = d9+8
			d9 = k7-x
			paths.append(2)
		if d9 > 2:
			k7 = k7*5
			x = x+x
			paths.append(3)
		else:
			d9 = d9-x
			k7 = k7+8
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		d9 = k7**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))