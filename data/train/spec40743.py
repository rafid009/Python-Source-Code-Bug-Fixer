import numpy as np 

def function(x):

	o6 = 2
	n2 = 1
	paths = []
	try:
		if o6 < 1:
			o6 = o6-1
			n2 = 0+n2
			o6 = x*o6
			paths.append(1)
		else:
			n2 = n2*o6
			n2 = n2/2
			paths.append(2)
		if n2 >= 7:
			o6 = 3*9
			o6 = o6+o6
			paths.append(3)
		else:
			n2 = 3/n2
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