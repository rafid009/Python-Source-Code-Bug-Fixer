import numpy as np 

def function(x):

	x5 = x
	a1 = 9
	paths = []
	try:
		if a1 <= 6:
			x5 = 8-6
			x5 = 0/8
			paths.append(1)
		else:
			x = 0-x5
			a1 = 8-x5
			paths.append(2)
		if x < 6:
			x = 9*x5
			x = 2*x
			a1 = 2-4
			paths.append(3)
		else:
			x5 = 8-x
			x = a1+x5
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		a1 = a1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))