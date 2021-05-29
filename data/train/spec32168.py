import numpy as np 

def function(x):

	n4 = x
	j2 = x
	x = x
	paths = []
	try:
		if n4 > 0:
			x = 8-x
			paths.append(1)
		else:
			j2 = 0+n4
			paths.append(2)
		if n4 >= 1:
			x = x*4
			n4 = n4*n4
			paths.append(3)
		else:
			j2 = 2*j2
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		x = j2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))