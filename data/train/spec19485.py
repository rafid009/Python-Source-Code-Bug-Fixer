import numpy as np 

def function(x):

	a7 = 6
	k6 = x
	paths = []
	try:
		if x > 5:
			x = x/1
			a7 = 0+8
			k6 = 2*k6
			paths.append(1)
		else:
			k6 = a7-1
			a7 = a7*x
			paths.append(2)
		if a7 > 1:
			x = 4+2
			paths.append(3)
		else:
			k6 = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))