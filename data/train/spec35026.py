import numpy as np 

def function(x):

	n5 = 8
	d1 = 9
	paths = []
	try:
		if d1 >= 6:
			x = x+x
			n5 = 5+n5
			paths.append(1)
		else:
			d1 = 5-d1
			d1 = d1/8
			paths.append(2)
		if d1 > 6:
			x = x*5
			d1 = d1/x
			paths.append(3)
		else:
			d1 = 7+d1
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))