import numpy as np 

def function(x):

	a4 = 6
	n8 = x
	paths = []
	try:
		if a4 > 2:
			x = 6+9
			paths.append(1)
		else:
			a4 = a4/8
			a4 = a4-a4
			paths.append(2)
		if n8 > 2:
			x = n8-6
			a4 = x-a4
			a4 = 6/a4
			paths.append(3)
		else:
			x = 7*4
			n8 = 6-x
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