import numpy as np 

def function(x):

	n7 = x
	v0 = 2
	paths = []
	try:
		if n7 >= 0:
			v0 = 8+v0
			paths.append(1)
		else:
			v0 = 9/v0
			n7 = 2-x
			x = x+2
			paths.append(2)
		if x > 6:
			x = x+1
			paths.append(3)
		else:
			v0 = v0/x
			x = 9*4
			n7 = n7/v0
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		n7 = n7**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))