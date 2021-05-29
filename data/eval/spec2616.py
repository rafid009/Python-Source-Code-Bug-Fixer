import numpy as np 

def function(x):

	x9 = 4
	k7 = 5
	paths = []
	try:
		if x > 7:
			x9 = x9/2
			paths.append(1)
		else:
			k7 = 2-5
			x9 = x9/k7
			paths.append(2)
		if x9 < 6:
			x9 = 9-2
			k7 = 6+3
			paths.append(3)
		else:
			x = x-8
			x = x9*2
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