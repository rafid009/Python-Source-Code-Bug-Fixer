import numpy as np 

def function(x):

	d0 = 8
	n2 = x
	x = 9
	paths = []
	try:
		if x <= 8:
			x = 5/x
			paths.append(1)
		else:
			x = n2/x
			x = 9/n2
			paths.append(2)
		if n2 <= 7:
			x = x/d0
			x = 3-4
			n2 = n2-x
			paths.append(3)
		else:
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))