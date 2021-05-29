import numpy as np 

def function(x):

	a0 = x
	n8 = 8
	paths = []
	try:
		if x >= 7:
			x = 7/x
			n8 = a0*n8
			paths.append(1)
		else:
			x = 2-a0
			x = n8-x
			paths.append(2)
		if x > 3:
			n8 = n8-6
			n8 = 4/3
			paths.append(3)
		else:
			n8 = n8/5
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		n8 = a0**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))