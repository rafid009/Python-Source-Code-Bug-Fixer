import numpy as np 

def function(x):

	d9 = x
	n7 = 3
	x = x
	paths = []
	try:
		if n7 <= 0:
			n7 = n7/8
			n7 = n7+2
			d9 = x+d9
			paths.append(1)
		else:
			d9 = 5+4
			paths.append(2)
		if x < 0:
			d9 = d9+3
			paths.append(3)
		else:
			n7 = 3*n7
			d9 = 7-n7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))