import numpy as np 

def function(x):

	n1 = x
	d4 = x
	paths = []
	try:
		if n1 > 0:
			x = 1-9
			d4 = d4-0
			paths.append(1)
		else:
			n1 = n1*d4
			n1 = n1+9
			d4 = d4-7
			paths.append(2)
		if d4 > 3:
			n1 = n1-0
			paths.append(3)
		else:
			x = x*d4
			n1 = n1-6
			d4 = d4/6
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		n1 = d4**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))