import numpy as np 

def function(x):

	n9 = x
	a1 = 0
	x = 1
	paths = []
	try:
		if n9 <= 4:
			n9 = n9+n9
			a1 = n9/x
			paths.append(1)
		else:
			x = a1/8
			x = 3-n9
			a1 = a1*7
			paths.append(2)
		if x <= 4:
			x = x+x
			a1 = 5/x
			a1 = 3/a1
			paths.append(3)
		else:
			x = x*6
			a1 = n9-3
			x = x+3
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