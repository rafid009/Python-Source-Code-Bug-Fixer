import numpy as np 

def function(x):

	n8 = 7
	o1 = x
	paths = []
	try:
		if o1 < 9:
			n8 = o1*8
			paths.append(1)
		else:
			n8 = o1*3
			paths.append(2)
		if x >= 8:
			o1 = o1/5
			paths.append(3)
		else:
			o1 = o1*x
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		x = n8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))