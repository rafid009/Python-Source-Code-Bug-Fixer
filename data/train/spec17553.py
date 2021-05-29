import numpy as np 

def function(x):

	f6 = x
	a2 = x
	paths = []
	try:
		if x >= 9:
			f6 = f6+0
			f6 = 7-1
			paths.append(1)
		else:
			a2 = a2/x
			f6 = x+f6
			paths.append(2)
		if x < 9:
			f6 = f6+x
			f6 = f6*3
			paths.append(3)
		else:
			x = x-1
			x = 9-f6
			a2 = a2/f6
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