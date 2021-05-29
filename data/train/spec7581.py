import numpy as np 

def function(x):

	o9 = 5
	n9 = x
	paths = []
	try:
		if o9 >= 2:
			x = o9*x
			paths.append(1)
		else:
			o9 = x+o9
			paths.append(2)
		if n9 < 7:
			x = o9-n9
			o9 = 4-n9
			paths.append(3)
		else:
			n9 = n9-o9
			n9 = 2*n9
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		n9 = n9**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))