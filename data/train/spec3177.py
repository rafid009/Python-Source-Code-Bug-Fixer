import numpy as np 

def function(x):

	d5 = x
	n2 = 2
	paths = []
	try:
		if n2 < 4:
			n2 = 7/d5
			n2 = 5+d5
			paths.append(1)
		else:
			x = 7/x
			paths.append(2)
		if d5 < 9:
			d5 = 1/x
			n2 = n2/d5
			n2 = n2/8
			paths.append(3)
		else:
			n2 = n2/4
			d5 = 7-d5
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		d5 = n2**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))