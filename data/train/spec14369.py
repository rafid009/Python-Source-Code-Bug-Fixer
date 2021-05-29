import numpy as np 

def function(x):

	a9 = x
	f4 = 0
	paths = []
	try:
		if x < 8:
			a9 = a9+9
			x = 7-x
			paths.append(1)
		else:
			f4 = 0+5
			paths.append(2)
		if a9 >= 0:
			x = x+9
			x = 0*f4
			paths.append(3)
		else:
			a9 = a9-a9
			a9 = a9-x
			a9 = 2+a9
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))