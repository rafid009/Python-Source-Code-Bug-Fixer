import numpy as np 

def function(x):

	a0 = 4
	k7 = 5
	paths = []
	try:
		if k7 <= 3:
			a0 = 5-1
			paths.append(1)
		else:
			k7 = 6/2
			x = a0-x
			paths.append(2)
		if x <= 7:
			x = 6+x
			paths.append(3)
		else:
			k7 = 2/k7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))