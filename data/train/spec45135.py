import numpy as np 

def function(x):

	n3 = 0
	d4 = x
	paths = []
	try:
		if x <= 9:
			n3 = d4+x
			x = x+3
			paths.append(1)
		else:
			d4 = d4+8
			paths.append(2)
		if n3 > 0:
			d4 = d4+x
			d4 = d4+8
			d4 = d4*4
			paths.append(3)
		else:
			d4 = d4-9
			n3 = n3/4
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		n3 = d4**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))