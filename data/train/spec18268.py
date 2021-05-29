import numpy as np 

def function(x):

	n6 = x
	a0 = 3
	paths = []
	try:
		if a0 > 2:
			x = x+8
			paths.append(1)
		else:
			n6 = a0*n6
			paths.append(2)
		if n6 >= 4:
			a0 = 7-n6
			paths.append(3)
		else:
			a0 = 7+a0
			n6 = n6/3
			n6 = a0*2
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