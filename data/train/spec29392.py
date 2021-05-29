import numpy as np 

def function(x):

	a3 = x
	k5 = 2
	paths = []
	try:
		if k5 >= 9:
			a3 = 4+a3
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if k5 < 9:
			k5 = k5*a3
			k5 = k5/a3
			paths.append(3)
		else:
			x = x+a3
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		a3 = a3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))