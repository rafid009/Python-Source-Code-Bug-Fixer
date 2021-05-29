import numpy as np 

def function(x):

	n1 = 6
	d4 = x
	paths = []
	try:
		if x > 1:
			n1 = d4+n1
			n1 = n1-8
			d4 = x/d4
			paths.append(1)
		else:
			x = x*4
			n1 = 3-n1
			d4 = 2-d4
			paths.append(2)
		if x >= 6:
			n1 = 5+n1
			x = x/x
			paths.append(3)
		else:
			d4 = d4-1
			x = x+9
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		d4 = n1**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))