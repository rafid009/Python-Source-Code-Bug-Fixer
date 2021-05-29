import numpy as np 

def function(x):

	n5 = 8
	a4 = x
	x = x
	paths = []
	try:
		if x >= 2:
			x = x-a4
			x = a4*3
			paths.append(1)
		else:
			n5 = n5/4
			x = a4-x
			a4 = a4*a4
			paths.append(2)
		if x <= 4:
			n5 = 4*n5
			a4 = n5/n5
			n5 = 4-n5
			paths.append(3)
		else:
			a4 = 6-n5
			a4 = 1-6
			a4 = a4+0
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		n5 = a4**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))