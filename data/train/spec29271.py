import numpy as np 

def function(x):

	v2 = 8
	n8 = x
	paths = []
	try:
		if v2 > 6:
			n8 = n8+2
			paths.append(1)
		else:
			n8 = n8*4
			paths.append(2)
		if v2 >= 8:
			v2 = x+v2
			paths.append(3)
		else:
			n8 = n8/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))