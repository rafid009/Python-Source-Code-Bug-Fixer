import numpy as np 

def function(x):

	v7 = x
	n8 = 1
	paths = []
	try:
		if v7 >= 8:
			n8 = n8+6
			v7 = x*x
			paths.append(1)
		else:
			x = x-6
			x = x*n8
			paths.append(2)
		if x >= 9:
			x = x+x
			paths.append(3)
		else:
			n8 = n8+v7
			n8 = x-5
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