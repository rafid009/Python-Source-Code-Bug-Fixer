import numpy as np 

def function(x):

	n2 = 2
	o4 = x
	paths = []
	try:
		if n2 > 2:
			n2 = o4*x
			o4 = o4+9
			paths.append(1)
		else:
			n2 = 7-2
			paths.append(2)
		if x <= 8:
			o4 = 6/o4
			x = 3-x
			n2 = n2/n2
			paths.append(3)
		else:
			x = n2+o4
			n2 = n2*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))