import numpy as np 

def function(x):

	a2 = 9
	i0 = x
	paths = []
	try:
		if a2 >= 8:
			a2 = 0*0
			paths.append(1)
		else:
			a2 = 6/8
			x = 0/x
			paths.append(2)
		if a2 >= 2:
			a2 = 2*a2
			paths.append(3)
		else:
			x = i0*x
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x = i0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))