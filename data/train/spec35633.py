import numpy as np 

def function(x):

	n1 = x
	o8 = x
	paths = []
	try:
		if n1 > 7:
			x = 7-x
			o8 = o8+x
			n1 = n1/3
			paths.append(1)
		else:
			o8 = 0-o8
			n1 = 6/n1
			paths.append(2)
		if n1 < 8:
			n1 = x*8
			o8 = o8-x
			paths.append(3)
		else:
			n1 = n1-n1
			x = 6+o8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o8 = x**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))