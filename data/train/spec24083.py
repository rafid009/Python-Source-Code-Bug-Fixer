import numpy as np 

def function(x):

	q8 = x
	a0 = 7
	paths = []
	try:
		if x >= 4:
			q8 = a0*6
			paths.append(1)
		else:
			a0 = 6-6
			paths.append(2)
		if q8 <= 1:
			q8 = q8*8
			paths.append(3)
		else:
			a0 = 5-a0
			x = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))