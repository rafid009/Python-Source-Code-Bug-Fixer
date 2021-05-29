import numpy as np 

def function(x):

	f5 = 3
	a0 = 7
	paths = []
	try:
		if x >= 6:
			x = 6/3
			f5 = f5-4
			f5 = f5*9
			paths.append(1)
		else:
			f5 = 9+f5
			paths.append(2)
		if f5 < 7:
			x = x/3
			paths.append(3)
		else:
			f5 = 5*x
			x = f5+5
			a0 = 9/f5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))