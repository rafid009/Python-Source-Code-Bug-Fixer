import numpy as np 

def function(x):

	j9 = x
	a1 = 2
	paths = []
	try:
		if a1 > 0:
			x = x-6
			a1 = 6-a1
			paths.append(1)
		else:
			x = 8*8
			a1 = 7/a1
			paths.append(2)
		if j9 < 0:
			x = j9*5
			paths.append(3)
		else:
			a1 = x/9
			a1 = a1-x
			x = j9+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))