import numpy as np 

def function(x):

	n9 = x
	x0 = 0
	paths = []
	try:
		if x > 4:
			x = x-0
			paths.append(1)
		else:
			n9 = n9+6
			paths.append(2)
		if n9 > 1:
			x0 = n9/x
			x0 = x0/6
			paths.append(3)
		else:
			n9 = x0+x
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		x0 = n9**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))