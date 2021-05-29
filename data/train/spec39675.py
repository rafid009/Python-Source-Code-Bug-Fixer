import numpy as np 

def function(x):

	n5 = x
	v4 = x
	paths = []
	try:
		if x < 0:
			n5 = n5/2
			paths.append(1)
		else:
			n5 = n5*8
			paths.append(2)
		if x <= 2:
			x = 4/x
			v4 = 1+v4
			n5 = n5/1
			paths.append(3)
		else:
			n5 = n5*x
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))