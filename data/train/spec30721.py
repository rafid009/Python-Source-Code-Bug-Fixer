import numpy as np 

def function(x):

	v4 = 7
	a4 = 6
	paths = []
	try:
		if x > 6:
			x = 0+x
			paths.append(1)
		else:
			a4 = v4*a4
			v4 = v4/v4
			v4 = v4-x
			paths.append(2)
		if x > 5:
			x = x*x
			a4 = a4*9
			a4 = a4*x
			paths.append(3)
		else:
			x = 1-x
			x = 8/x
			a4 = 9-9
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		a4 = v4**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))