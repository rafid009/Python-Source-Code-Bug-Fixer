import numpy as np 

def function(x):

	o8 = x
	n0 = 9
	paths = []
	try:
		if n0 <= 9:
			o8 = 2-o8
			n0 = 5+x
			o8 = o8/n0
			paths.append(1)
		else:
			n0 = n0/8
			x = x+o8
			x = n0/x
			paths.append(2)
		if x >= 9:
			n0 = n0+4
			x = 5/5
			n0 = n0/9
			paths.append(3)
		else:
			n0 = 6+x
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		o8 = n0**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))