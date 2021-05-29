import numpy as np 

def function(x):

	a2 = 6
	x4 = x
	paths = []
	try:
		if x < 1:
			x4 = 8*7
			paths.append(1)
		else:
			a2 = a2+1
			a2 = 9+a2
			x = 0+x
			paths.append(2)
		if x < 6:
			a2 = a2-6
			paths.append(3)
		else:
			x4 = a2/x4
			x4 = 4-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))