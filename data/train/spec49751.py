import numpy as np 

def function(x):

	n8 = 5
	d0 = 6
	x = x
	paths = []
	try:
		if n8 < 8:
			x = x*5
			paths.append(1)
		else:
			x = n8/n8
			paths.append(2)
		if n8 <= 6:
			n8 = x+x
			paths.append(3)
		else:
			n8 = 6+8
			d0 = 5*d0
			n8 = 7-n8
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		d0 = n8**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))