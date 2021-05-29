import numpy as np 

def function(x):

	x5 = 0
	a5 = 9
	paths = []
	try:
		if a5 < 1:
			a5 = 9-6
			a5 = 4*4
			paths.append(1)
		else:
			a5 = a5*1
			x = x+3
			x5 = x-x
			paths.append(2)
		if a5 >= 8:
			a5 = x*a5
			x = 5+0
			paths.append(3)
		else:
			x5 = 0*a5
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x5 = a5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))