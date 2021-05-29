import numpy as np 

def function(x):

	a3 = x
	k5 = x
	paths = []
	try:
		if x >= 1:
			x = 1*x
			paths.append(1)
		else:
			x = x-4
			a3 = 1-x
			a3 = 8-a3
			paths.append(2)
		if k5 <= 5:
			a3 = 0-3
			a3 = a3*9
			paths.append(3)
		else:
			x = a3/x
			k5 = k5+5
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		k5 = a3**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))