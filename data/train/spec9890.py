import numpy as np 

def function(x):

	n5 = x
	d8 = 1
	paths = []
	try:
		if n5 > 9:
			d8 = d8+2
			paths.append(1)
		else:
			n5 = n5/9
			x = 4*8
			x = x+x
			paths.append(2)
		if n5 >= 0:
			d8 = d8+n5
			paths.append(3)
		else:
			x = x-0
			d8 = d8-d8
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))