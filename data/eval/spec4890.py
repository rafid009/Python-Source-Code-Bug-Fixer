import numpy as np 

def function(x):

	n2 = 9
	d9 = x
	x = x
	paths = []
	try:
		if d9 <= 9:
			x = d9*n2
			d9 = d9+3
			paths.append(1)
		else:
			d9 = 5+d9
			d9 = 3-d9
			paths.append(2)
		if d9 <= 5:
			n2 = 9+x
			n2 = 9/8
			paths.append(3)
		else:
			d9 = 4/2
			n2 = 7-n2
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		d9 = n2**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))