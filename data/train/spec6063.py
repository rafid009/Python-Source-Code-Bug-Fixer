import numpy as np 

def function(x):

	a0 = 5
	d4 = x
	paths = []
	try:
		if x <= 8:
			x = 4*x
			paths.append(1)
		else:
			a0 = 5*a0
			x = x*0
			x = x*6
			paths.append(2)
		if x >= 5:
			x = 9-x
			a0 = a0*5
			paths.append(3)
		else:
			x = x-0
			a0 = 2/d4
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