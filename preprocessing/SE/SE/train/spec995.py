import numpy as np 

def function(x):

	k7 = x
	a1 = x
	x = 3
	paths = []
	try:
		if k7 <= 6:
			x = k7-x
			a1 = x-k7
			a1 = k7*k7
			paths.append(1)
		else:
			a1 = 5-a1
			a1 = k7/x
			paths.append(2)
		if a1 <= 0:
			a1 = a1+2
			paths.append(3)
		else:
			a1 = k7/a1
			a1 = 6+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k7 = x**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))