import numpy as np 

def function(x):

	a7 = 8
	k2 = 4
	paths = []
	try:
		if a7 <= 2:
			x = 4/x
			paths.append(1)
		else:
			k2 = 1+k2
			x = 5*0
			x = x-9
			paths.append(2)
		if a7 >= 0:
			a7 = a7-9
			paths.append(3)
		else:
			k2 = 6*x
			k2 = 4-k2
			k2 = k2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))