import numpy as np 

def function(x):

	a1 = 7
	a2 = 0
	paths = []
	try:
		if x >= 6:
			a2 = a2+7
			a2 = a2-a2
			a1 = a1+7
			paths.append(1)
		else:
			a1 = 6*a1
			a1 = 1/2
			paths.append(2)
		if x <= 7:
			a2 = a2-x
			a1 = 8*a1
			a2 = 9*a2
			paths.append(3)
		else:
			a2 = a2*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))