import numpy as np 

def function(x):

	o8 = 1
	n1 = 6
	paths = []
	try:
		if x >= 6:
			n1 = n1-1
			o8 = 7-o8
			o8 = x/o8
			paths.append(1)
		else:
			x = x-0
			n1 = n1-x
			x = o8*x
			paths.append(2)
		if n1 > 4:
			n1 = n1-5
			paths.append(3)
		else:
			x = x*4
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