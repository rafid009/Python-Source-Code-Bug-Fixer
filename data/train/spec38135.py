import numpy as np 

def function(x):

	f0 = 9
	a2 = 6
	paths = []
	try:
		if f0 <= 3:
			f0 = f0-x
			f0 = f0+x
			paths.append(1)
		else:
			x = x-f0
			x = 8+x
			x = 3+x
			paths.append(2)
		if x >= 3:
			f0 = 6-x
			paths.append(3)
		else:
			f0 = 7+f0
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