import numpy as np 

def function(x):

	n5 = 8
	d7 = x
	paths = []
	try:
		if n5 >= 4:
			d7 = 5-d7
			d7 = d7+d7
			paths.append(1)
		else:
			x = d7-4
			n5 = d7*n5
			n5 = n5+8
			paths.append(2)
		if n5 > 5:
			d7 = d7/x
			d7 = d7*4
			paths.append(3)
		else:
			n5 = d7-8
			x = x/6
			x = x/n5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))