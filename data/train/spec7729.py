import numpy as np 

def function(x):

	o5 = x
	n4 = x
	paths = []
	try:
		if x <= 1:
			n4 = 3/n4
			n4 = 0-7
			o5 = 0-x
			paths.append(1)
		else:
			x = 4-x
			paths.append(2)
		if o5 >= 9:
			o5 = n4*2
			o5 = o5+4
			x = 2*x
			paths.append(3)
		else:
			x = 4*4
			o5 = o5+o5
			o5 = o5+o5
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x = o5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))