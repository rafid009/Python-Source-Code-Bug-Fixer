import numpy as np 

def function(x):

	n8 = 4
	h3 = 5
	paths = []
	try:
		if n8 >= 0:
			n8 = n8+7
			n8 = n8/n8
			paths.append(1)
		else:
			n8 = 5*5
			n8 = 2-n8
			x = 5+x
			paths.append(2)
		if x >= 2:
			x = x-n8
			paths.append(3)
		else:
			n8 = x/3
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