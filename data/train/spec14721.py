import numpy as np 

def function(x):

	x3 = x
	a0 = 3
	paths = []
	try:
		if x3 >= 9:
			a0 = a0/5
			paths.append(1)
		else:
			x3 = x3-8
			paths.append(2)
		if x < 7:
			x = 6-x
			a0 = 6/x
			x = 6+x
			paths.append(3)
		else:
			x3 = a0+x3
			a0 = 2-x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		a0 = a0**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))