import numpy as np 

def function(x):

	n9 = x
	a7 = 0
	paths = []
	try:
		if a7 >= 0:
			x = 3*n9
			x = x+x
			n9 = 4+0
			paths.append(1)
		else:
			n9 = n9/n9
			paths.append(2)
		if a7 < 3:
			a7 = 3+a7
			n9 = n9/8
			paths.append(3)
		else:
			x = n9/5
			n9 = n9+n9
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