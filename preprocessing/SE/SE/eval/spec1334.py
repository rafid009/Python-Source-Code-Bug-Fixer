import numpy as np 

def function(x):

	l9 = x
	a4 = x
	paths = []
	try:
		if a4 < 6:
			x = l9+x
			a4 = a4/4
			paths.append(1)
		else:
			x = 2-x
			a4 = a4+a4
			paths.append(2)
		if a4 >= 3:
			a4 = a4+4
			paths.append(3)
		else:
			a4 = a4-7
			a4 = 4*a4
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		a4 = a4**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))