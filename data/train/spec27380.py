import numpy as np 

def function(x):

	n1 = 4
	o8 = 8
	paths = []
	try:
		if o8 <= 3:
			o8 = 6+o8
			n1 = o8/x
			x = n1*3
			paths.append(1)
		else:
			x = x+n1
			paths.append(2)
		if x >= 3:
			o8 = o8*4
			x = x+o8
			x = x*o8
			paths.append(3)
		else:
			n1 = 6+5
			x = 7-x
			n1 = n1-x
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		x = n1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))