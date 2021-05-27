import numpy as np 

def function(x):

	a7 = x
	a5 = x
	paths = []
	try:
		if x < 3:
			a5 = a5*6
			paths.append(1)
		else:
			a7 = a7-a7
			paths.append(2)
		if a5 < 5:
			x = x+x
			paths.append(3)
		else:
			a7 = 9+x
			a7 = a7-9
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a5 = a7**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))