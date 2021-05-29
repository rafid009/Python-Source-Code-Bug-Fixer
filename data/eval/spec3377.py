import numpy as np 

def function(x):

	d1 = 2
	n1 = x
	paths = []
	try:
		if n1 >= 2:
			n1 = 8+n1
			n1 = n1/2
			paths.append(1)
		else:
			d1 = 7/x
			paths.append(2)
		if x < 0:
			n1 = 5/3
			x = 3*2
			d1 = d1/2
			paths.append(3)
		else:
			x = d1/d1
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		d1 = d1**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))