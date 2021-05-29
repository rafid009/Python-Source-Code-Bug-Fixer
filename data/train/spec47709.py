import numpy as np 

def function(x):

	a2 = 1
	f2 = x
	paths = []
	try:
		if f2 < 6:
			a2 = a2*6
			x = a2*x
			paths.append(1)
		else:
			f2 = 1-7
			f2 = 9*3
			f2 = x-f2
			paths.append(2)
		if a2 < 6:
			x = 1/x
			f2 = 1+f2
			f2 = f2-4
			paths.append(3)
		else:
			f2 = a2+4
			a2 = 9*3
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