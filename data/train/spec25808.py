import numpy as np 

def function(x):

	n8 = 1
	a4 = x
	paths = []
	try:
		if x > 4:
			n8 = n8-2
			paths.append(1)
		else:
			n8 = 1*n8
			a4 = x+2
			paths.append(2)
		if x < 0:
			a4 = a4-1
			paths.append(3)
		else:
			x = x+8
			x = x+9
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))