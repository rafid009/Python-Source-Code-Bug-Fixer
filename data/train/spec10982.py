import numpy as np 

def function(x):

	a7 = x
	i9 = 3
	paths = []
	try:
		if x > 2:
			a7 = x+4
			paths.append(1)
		else:
			a7 = 6+a7
			i9 = i9-4
			a7 = a7+2
			paths.append(2)
		if a7 < 8:
			i9 = i9*i9
			x = x*a7
			paths.append(3)
		else:
			a7 = a7/2
			a7 = 6-i9
			x = a7-6
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))