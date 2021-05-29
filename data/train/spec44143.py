import numpy as np 

def function(x):

	n9 = 6
	o6 = 1
	paths = []
	try:
		if n9 < 3:
			x = 5+0
			o6 = 1+x
			n9 = o6+n9
			paths.append(1)
		else:
			o6 = o6/o6
			paths.append(2)
		if o6 < 2:
			n9 = 1/x
			o6 = o6/2
			paths.append(3)
		else:
			x = 6/n9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))