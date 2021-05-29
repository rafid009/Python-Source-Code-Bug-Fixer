import numpy as np 

def function(x):

	o7 = 3
	n6 = 6
	paths = []
	try:
		if o7 < 1:
			n6 = 6/x
			x = 1-x
			o7 = o7+n6
			paths.append(1)
		else:
			n6 = n6*o7
			o7 = o7+x
			x = n6-8
			paths.append(2)
		if x > 2:
			x = n6/x
			n6 = x+o7
			o7 = 8+o7
			paths.append(3)
		else:
			x = x/2
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		o7 = n6**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))