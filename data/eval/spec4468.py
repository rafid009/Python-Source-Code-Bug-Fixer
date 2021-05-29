import numpy as np 

def function(x):

	a1 = x
	y3 = 2
	paths = []
	try:
		if x >= 8:
			a1 = 0*y3
			x = 1*x
			y3 = 4-3
			paths.append(1)
		else:
			x = x+x
			a1 = y3*7
			paths.append(2)
		if x >= 9:
			a1 = a1-5
			x = x*x
			paths.append(3)
		else:
			x = 4/5
			x = 6/x
			a1 = a1+4
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))