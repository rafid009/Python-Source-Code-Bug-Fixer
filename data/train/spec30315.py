import numpy as np 

def function(x):

	o7 = x
	n3 = 3
	paths = []
	try:
		if o7 <= 6:
			n3 = n3+n3
			x = x+2
			o7 = 0/n3
			paths.append(1)
		else:
			x = x+n3
			o7 = x-3
			paths.append(2)
		if n3 > 5:
			x = x/7
			x = x+o7
			o7 = o7+4
			paths.append(3)
		else:
			o7 = o7/3
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