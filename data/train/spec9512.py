import numpy as np 

def function(x):

	t4 = x
	n0 = x
	x = 2
	paths = []
	try:
		if t4 >= 6:
			n0 = 3/x
			n0 = n0-8
			paths.append(1)
		else:
			x = x-t4
			x = 0+5
			paths.append(2)
		if x >= 4:
			n0 = n0*9
			x = x*0
			x = 9*x
			paths.append(3)
		else:
			x = 6*x
			x = x-4
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		n0 = t4**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))