import numpy as np 

def function(x):

	n8 = x
	a0 = 5
	paths = []
	try:
		if x > 6:
			a0 = a0+9
			a0 = a0*a0
			a0 = a0-a0
			paths.append(1)
		else:
			n8 = x*7
			a0 = 2/x
			paths.append(2)
		if a0 > 3:
			x = x+4
			a0 = a0+0
			a0 = n8+n8
			paths.append(3)
		else:
			n8 = a0*n8
			n8 = n8+0
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		x = a0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))