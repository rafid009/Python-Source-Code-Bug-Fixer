import numpy as np 

def function(x):

	a0 = x
	f9 = 8
	paths = []
	try:
		if a0 <= 0:
			f9 = 1-a0
			paths.append(1)
		else:
			a0 = a0-1
			a0 = a0*x
			paths.append(2)
		if a0 <= 9:
			f9 = f9-f9
			f9 = f9-x
			paths.append(3)
		else:
			x = x-x
			a0 = 2+a0
			f9 = f9+2
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		a0 = f9**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))