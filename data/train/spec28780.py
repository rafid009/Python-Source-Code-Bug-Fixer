import numpy as np 

def function(x):

	o4 = x
	n9 = x
	paths = []
	try:
		if x >= 9:
			o4 = 4-o4
			paths.append(1)
		else:
			n9 = x+0
			x = x-6
			paths.append(2)
		if n9 >= 0:
			o4 = x-7
			n9 = 8+9
			paths.append(3)
		else:
			o4 = n9/x
			n9 = 8+6
			n9 = 4+8
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		x = o4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))